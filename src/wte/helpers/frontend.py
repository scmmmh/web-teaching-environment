# -*- coding: utf-8 -*-
u"""
###############################################################
:mod:`wte.helpers.frontend` -- Helpers for the frontend display
###############################################################

The :mod:`~wte.helpers.frontend` module provides helper functionality used to
render the frontend page displays.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import json
import re

from genshi.builder import tag, Markup


def html_id(text):
    u"""Turns a given text into a valid HTML id attribute value. Removes
    spaces and full-stops.

    :param text: The text to convert
    :type text: `unicode`
    :return: The corresponding HTML id
    :rtype: `unicode`
    """
    return text.replace(' ', '_').replace('.', '_')


CODEMIRROR_MODES = {'text/html': ['javascript',
                                  'css',
                                  'xml',
                                  'htmlmixed',
                                  ('../addon/fold/', 'xml-fold'),
                                  ('../addon/edit', 'matchtags')],
                    'text/css': ['css',
                                 ('../addon/edit', 'matchbrackets'),
                                 ('../addon/lint', 'lint'),
                                 ('../addon/lint', 'csslint'),
                                 ('../addon/lint', 'css-lint')],
                    'text/javascript': ['javascript',
                                        ('../addon/edit', 'matchbrackets'),
                                        ('../addon/lint', 'lint'),
                                        ('../addon/lint', 'jshint'),
                                        ('../addon/lint', 'javascript-lint')],
                    'application/javascript': ['javascript',
                                               ('../addon/edit', 'matchbrackets'),
                                               ('../addon/lint', 'lint'),
                                               ('../addon/lint', 'jshint'),
                                               ('../addon/lint', 'javascript-lint')],
                    'text/x-rst': ['python',
                                   'stex',
                                   ('../addon/mode', 'overlay'),
                                   'rst']}


def codemirror_scripts(request, mimetypes):
    u"""Generates the ``<script>`` tags necessary to load the CodeMirror mode
    JS files for the given list of ``mimetypes``.

    :param request: The request to use for generating URLs
    :type request: `~pyramid.request.Request`
    :param mimetypes: The mimetypes to load the CodeMirror modes for
    :type mimetypes: `list` of `unicode`
    :return: The necessary ``<script>`` tags
    """
    modes = []
    for mimetype in mimetypes:
        if mimetype in CODEMIRROR_MODES:
            for mode in CODEMIRROR_MODES[mimetype]:
                if isinstance(mode, tuple):
                    modes.append(mode)
                else:
                    modes.append((mode, mode))
    scripts = [request.static_url('wte:static/js/codemirror/codemirror.js')]
    for mode in modes:
        script = request.static_url('wte:static/js/codemirror/mode/%s/%s.js' % mode)
        if script not in scripts:
            scripts.append(script)
    return tag([tag.script(src=s) for s in scripts])


CODEMIRROR_OPTIONS = {'text/html': {'matchTags': True},
                      'text/css': {'gutters': ['CodeMirror-lint-markers'],
                                   'matchBrackets': True,
                                   'lint': True},
                      'text/javascript': {'lint': True,
                                          'gutters': ['CodeMirror-lint-markers'],
                                          'matchBrackets': True},
                      'application/javascript': {'gutters': ['CodeMirror-lint-markers'],
                                                 'matchBrackets': True,
                                                 'lint': True}}


def codemirror_options(mimetype):
    u"""Generates a JSON representation of CodeMirror options that are valid
    for the given ``mimetype``.

    :param mimetype: The mimetype to generate CodeMirror options for
    :type mimetype: `unicode`
    :return: The JSON representation of options
    """
    if mimetype in CODEMIRROR_OPTIONS:
        return json.dumps(CODEMIRROR_OPTIONS[mimetype])
    else:
        return json.dumps({})


def page_pagination(request, part):
    u"""Generates the pagination UI for the individual page display of a
    :class:`~wte.models.Part`.

    :param request: The current request
    :type request: :class:`~pyramid.request.Request`
    :param part: The current parte to display pagination for
    :type part: :class:`~wte.models.Part`
    :return: The resulting HTML markup
    """
    prev_page = None
    next_page = None
    state = 0
    for child in part.parent.children:
        if state == 0 and child != part:
            prev_page = child
        elif state == 0 and child == part:
            state = 1
        elif state == 1:
            next_page = child
            break
    items = []
    if prev_page:
        items.append(tag.li(tag.a(Markup('&laquo; Previous page'),
                                  href=request.route_url('part.view',
                                                         pid=prev_page.id))))
    else:
        items.append(tag.li(Markup('&laquo; Previous page'),
                            class_='disabled'))
    if next_page:
        items.append(tag.li(tag.a(Markup('Next page &raquo;'),
                                  href=request.route_url('part.view',
                                                         pid=next_page.id))))
    else:
        items.append(tag.li(Markup('Previous page &raquo;'),
                            class_='disabled'))
    return tag.ul(items,
                  class_='pagination')


def primary_filename(progress):
    u"""Returns the filename of the first :class:`~wte.models.File` from the
    :class:`~wte.models.UserPartProgress` that has the mimetype "text/html".

    :param progress: The :class:`~wte.models.UserPartProgress` to get the files
                     from
    :type progress: :class:`~wte.models.UserPartProgress`
    :return: The filename as a string or the empty string
    :rtype: `unicode`
    """
    files = [f for f in progress.files if f.mimetype == 'text/html']
    if files:
        return files[0].filename
    else:
        return ''


def confirm_action(title, message, cancel, ok):
    u"""Generates a confirmation JSON object for use with the jQuery.postLink() plugin.

    :param title: The title of the confirmation dialog box
    :type title: ``unicode``
    :param message: The main message to show
    :type message: ``unicode``
    :param cancel: The cancel button's settings
    :type cancel: ``dict`` or ``unicode``
    :param ok: The ok button's settings
    :type ok: ``dict`` or ``unicode``
    :return: JSON object
    :rtype: ``unicode``
    """
    return json.dumps({'title': title,
                       'msg': message,
                       'cancel': cancel if isinstance(cancel, dict) else {'label': cancel},
                       'ok': ok if isinstance(ok, dict) else {'label': ok}})


def confirm_delete(obj_type, title, has_parts=False):
    u"""Generates the confirmation JSON object for use with the jQuery.postLink() plugin.

    :param obj_type: The type of object that is being deleted
    :type obj_type: ``unicode``
    :param title: The title of the object that is being delete
    :type title: ``unicode``
    :param has_parts: Whether to add the suffix " and all its parts"
    :type has_parts: ``bool``
    :return: JSON object
    :rtype: ``unicode``
    """
    msg = 'Please confirm that you wish to delete the %s "%s"' % (obj_type, title)
    if has_parts:
        msg = '%s and all its parts.' % (msg)
    else:
        msg = '%s.' % (msg)
    return confirm_action('Delete this %s' % (obj_type),
                          msg,
                          "Don't delete",
                          {'label': 'Delete',
                           'class_': 'alert'})


def part_summary(part):
    u"""Generates summary text for a :class:`~wte.models.Part` by extracting the first HTML element
    from the ``compiled_content``. Due to the use of ReST, this should in most cases be the first
    paragraph.

    :param part: The :class:`~wte.models.Part` to generate the summary for
    :type part: :class:`~wte.models.Part`
    :return: The first HTML element
    :rtype: :class:`~genshi.builder.Markup`
    """
    content = part.compiled_content
    if content:
        m = re.search(r'<([a-zA-Z+])>', content)
        if m:
            start = content.find('<%s>' % (m.group(1)))
            end = content.find('</%s>' % (m.group(1))) + len(m.group(1)) + 3
            return Markup(content[start:end])
    return None


def menubar(menu, drop_down_menu_left=True, class_=None):
    u"""Generates a menu bar for a nested set of menu groups and menu items. Each menu group is specified as
    a ``dict`` with the following keys:

    * *group*: the name of the group
    * *items*: a list of menu item ``dict``

    Each menu item is specified as a ``dict``, which has the following keys:

    * *visible*: whether the element is displayed (``True``/``False``)
    * *label*: the label text to show
    * *href*: the href for the menu link
    * *class*: the CSS class to specify on the menu link [optional]
    * *icon*: a foundation icon to show for the menu link [optional]
    * *confirm*: confirmation text to show before the link is followed [optional]
    * *highlight*: whether to also show the item at the top-level of the menubar (``True``/``False``) [optional]

    Menu items that are marked as 'highlight: ``True`` and have an 'icon' set, will be shown at the top level of
    the menubar. All other items are shown in a drop-down menu.

    :param menu: The list of menu groups and items
    :type menu: ``list``
    :param drop_down_menu_left: Whether the drop-down menus should be left (True) or right-aligned (False)
    :type drop_down_menu_left: ``bool``
    :param class_: Additional CSS classes to add to the main menubar element
    :type class_: ``unicode``
    :return: The generated HTML elements
    :rtype: :class:`~genshi.builder.tag`"""
    full_menu = []
    highlight = []
    for group in menu:
        if(len(full_menu) > 0):
            full_menu.append(tag.li(class_='divider'))
        for item in group['items']:
            if item['visible']:
                full_menu.append(tag.li(tag.a(item['label'],
                                              href=item['href'],
                                              class_=item['class'] if 'class' in item else None,
                                              data_wte_confirm=item['confirm'] if 'confirm' in item else None,
                                              target=item['target'] if 'target' in item else None)))
                if 'highlight' in item and item['highlight'] and 'icon' in item:
                    item['group'] = group['group']
                    highlight.append(item)
    groups = []
    group = None
    for item in highlight:
        if group != item['group']:
            groups.append([])
            group = item['group']
        groups[len(groups) - 1].append(item)
    items = []
    for group in groups:
        if len(group) == 1:
            item = group[0]
            items.append(tag.li(tag.a(tag.span(class_=item['icon']), title=group[0]['label'],
                                      href=item['href'],
                                      class_=item['class'] if 'class' in item else None,
                                      data_wte_confirm=item['confirm'] if 'confirm' in item else None,
                                      target=item['target'] if 'target' in item else None)))
        else:
            sub_menu = []
            for item in group:
                sub_menu.append(tag.li(tag.a(item['label'],
                                             href=item['href'],
                                             class_=item['class'] if 'class' in item else None,
                                             data_wte_confirm=item['confirm'] if 'confirm' in item else None,
                                             target=item['target'] if 'target' in item else None)))
            items.append(tag.li(tag.div(tag.a(tag.span(class_=group[0]['icon']), href='#'),
                                        tag.ul(sub_menu),
                                        class_='menu',
                                        data_wte_menu_position='left' if drop_down_menu_left else 'right')))
    items.append(tag.li(tag.div(tag.a(tag.span(class_='fi-list'), href='#', title='All actions'),
                                tag.ul(full_menu),
                                class_='menu',
                                data_wte_menu_position='left' if drop_down_menu_left else 'right')))
    return tag.ul(items, class_='menubar %s' % (class_) if class_ else 'menubar')
