# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

HTML_EMPTY_ATTRS = set([
    'checked',
    'disabled',
    'readonly',
    'multiple',
    'selected',
    'nohref',
    'ismap',
    'declare',
    'defer',
])
HTML_OPTIONAL_END_TAGS = set([
    'area',
    'base',
    'body',
    'br',
    'col',
    'colgroup',
    'dd',
    'dt',
    'head',
    'hr',
    'html',
    'img',
    'input',
    'li',
    'link',
    'meta',
    'option',
    'p',
    'param',
    'tbody',
    'td',
    'tfoot',
    'th',
    'thead',
    'tr',
])
HTML_REQUIRED_END_TAGS = set(['script'])
HTML_CDATA_TAGS = set(('script', 'style'))
