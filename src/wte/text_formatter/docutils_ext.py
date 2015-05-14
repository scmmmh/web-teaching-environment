# -*- coding: utf-8 -*-
"""
######################################
:mod:`wte.text_formatter.docutils_ext`
######################################

This module contains docutils extensions (roles and directives) that provide
the additional formatting support required by the
:func:`~wte.text_formatter.compile_rst` function.
"""
import re

from docutils import nodes, utils
from docutils.parsers.rst import directives, roles, Directive
from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, TextLexer
from pyramid.request import Request


def init(settings):
    """Initialise and load the docutils extensions.
    """
    directives.register_directive('sourcecode', Pygments)
    roles.register_local_role('crossref', crossref_role)
    roles.register_local_role('code-html', inline_pygments_role)
    roles.register_local_role('code-css', inline_pygments_role)
    roles.register_local_role('code-javascript', inline_pygments_role)
    roles.register_local_role('code-python', inline_pygments_role)


class HtmlTitleFormatter(HtmlFormatter):
    """The :class:`~wte.text_formatter.docutils_ext.HtmlTitleFormatter` is
    an extension of :class:`pygments.formatters.HtmlFormatter` that supports
    adding the optional language name and filename to the top of the code
    block.
    """
    def __init__(self, language=None, filename=None, **kwargs):
        HtmlFormatter.__init__(self, **kwargs)
        self.language = language
        self.filename = filename

    def wrap(self, source, outfile):
        return self._wrap_code(source)

    def _wrap_code(self, source):
        yield 0, '<div class="source panel %s">' % (self.language if self.language else '')
        if self.language:
            yield 0, '<div class="title"><span class="main">%s</span>' % (self.language)
            if self.filename:
                yield 0, '<span class="filename">%s</span>' % (self.filename)
            yield 0, '</div><pre>'
        for i, t in source:
            yield i, t
        yield 0, '</pre></div>'


class Pygments(Directive):
    """The Pygments reStructuredText directive

    This fragment is a Docutils_ 0.5 directive that renders source code
    (to HTML only, currently) via Pygments.

    To use it, adjust the options below and copy the code into a module
    that you import on initialization.  The code then automatically
    registers a ``sourcecode`` directive that you can use instead of
    normal code blocks like this::

        .. sourcecode:: python

            My code goes here.

    If you want to have different code styles, e.g. one with line numbers
    and one without, add formatters with their names in the VARIANTS dict
    below.  You can invoke them instead of the DEFAULT one by using a
    directive option::

        .. sourcecode:: python
            :linenos:

            My code goes here.

    Look at the `directive documentation`_ to get all the gory details.

    .. _Docutils: http://docutils.sf.net/
    .. _directive documentation:
       http://docutils.sourceforge.net/docs/howto/rst-directives.html

    :copyright: Copyright 2006-2014 by the Pygments team, see AUTHORS.
    :license: BSD, see LICENSE for details.
    """
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    option_spec = {'filename': directives.unchanged}
    has_content = True

    def run(self):
        self.assert_has_content()
        try:
            lexer = get_lexer_by_name(self.arguments[0])
        except ValueError:
            # no lexer found - use the text one instead of an exception
            lexer = TextLexer()
        # take an arbitrary option if more than one is given
        formatter = HtmlTitleFormatter(language=lexer.name,
                                       filename=self.options['filename'] if 'filename' in self.options else None,
                                       noclasses=False,
                                       style='native',
                                       cssclass=u'source %s' % (lexer.name))
        parsed = highlight(u'\n'.join(self.content), lexer, formatter)
        return [nodes.raw('', parsed, format='html')]


CROSSREF_PATTERN = re.compile(r'([0-9]+)|(?:(.*)<([0-9]+)>)')


def crossref_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """The :func:`~wte.text_formatter.docutils_ext.crossref_role` function
    implements an additional docutils role that handles cross-references
    between :class:`~wte.models.Part`\ s.

    Usage in ReST is \:crossref\:\`part_id\` or \:crossref\:\`link text
    <part_id>\`.
    """
    from wte.models import (DBSession, Part)
    request = inliner.document.settings.pyramid_request
    result = []
    messages = []
    text = utils.unescape(text)
    match = re.match(CROSSREF_PATTERN, text)
    if match:
        groups = match.groups()
        target_id = groups[0] if groups[0] else groups[2]
        dbsession = DBSession()
        part = dbsession.query(Part).filter(Part.id == target_id).first()
        if part:
            result.append(nodes.reference(rawtext, groups[1] if groups[1] else part.title,
                                          internal=False,
                                          refuri=request.route_url('part.view',
                                                                   pid=target_id)))
        else:
            messages.append(inliner.reporter.warning('There is no target to link to for "%s"' % (text), line=lineno))
            result.append(inliner.problematic(rawtext, rawtext, messages[0]))
    else:
        messages.append(inliner.reporter.error('No valid link target identifier could be identified in "%s"' % (text),
                                               line=lineno))
        result.append(inliner.problematic(rawtext, rawtext, messages[0]))
    return result, messages


def inline_pygments_role(name, rawtext, text, lineno, inliner, options={}, content=[]):
    """The :func:`~wte.text_formatter.docutils_ext.inline_pygments_role`
    function provides a docutils role that handles inline code highlighting
    using Pygments. The name of the language to use for highlighting is taken
    from the name of the role (which must be formatted ``code-language_name`.
    """
    try:
        lexer = get_lexer_by_name(name[5:])
    except ValueError:
        lexer = TextLexer()
    formatter = HtmlFormatter(nowrap=True)
    parsed = highlight(text, lexer, formatter)
    return [nodes.raw('', '<span class="source">%s</span>' % (parsed), format='html')], []
