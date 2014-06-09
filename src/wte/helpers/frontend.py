# -*- coding: utf-8 -*-
u"""
###############################################################
:mod:`wte.helpers.frontend` -- Helpers for the frontend display
###############################################################

The :mod:`~wte.helpers.frontend` module provides helper functionality used to
render the frontend page displays.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""

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


CODEMIRROR_MODES = {'text/html': ['javascript', 'css', 'xml', 'htmlmixed'],
                    'text/css': ['css'],
                    'text/javascript': ['javascript']}


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
            modes.extend(CODEMIRROR_MODES[mimetype])
    return tag([tag.script(src=request.static_url('wte:static/js/codemirror/mode/%s/%s.js' % (mode, mode)))
                for mode in modes])


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
                                  href=request.route_url('part.view', mid=prev_page.module_id, pid=prev_page.id))))
    else:
        items.append(tag.li(Markup('&laquo; Previous page'),
                            class_='disabled'))
    if next_page:
        items.append(tag.li(tag.a(Markup('Next page &raquo;'),
                                  href=request.route_url('part.view', mid=next_page.module_id, pid=next_page.id))))
    else:
        items.append(tag.li(Markup('Previous page &raquo;'),
                            class_='disabled'))
    return tag.ul(items,
                  class_='pagination')
