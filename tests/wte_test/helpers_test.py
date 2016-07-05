# -*- coding: utf-8 -*-
"""
#################################
Unit tests for :mod:`wte.helpers`
#################################

Also contains tests for all sub-modules.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import json

from datetime import datetime


def test_lt():
    """Test the :func:`~wte.helpers.frontend.lt` function."""
    from wte.helpers.frontend import lt
    assert lt(1, 2) is True
    assert lt(2, 2) is False
    assert lt(2, 1) is False


def test_html_id():
    """Tests the :func:`~wte.helpers.frontend.html_id` function."""
    from wte.helpers.frontend import html_id
    assert html_id('filename.txt') == 'filename_txt'
    assert html_id('file name') == 'file_name'
    assert html_id('file name.txt') == 'file_name_txt'


def test_codemirror_scripts(request):
    """Test the codemirror scripts for a mimetype generation."""
    from wte.helpers.frontend import codemirror_scripts
    assert codemirror_scripts(request, ['text/html']) ==\
        ['http://localhost/static/js/codemirror/codemirror.js',
         'http://localhost/static/js/codemirror/mode/javascript/javascript.js',
         'http://localhost/static/js/codemirror/mode/css/css.js',
         'http://localhost/static/js/codemirror/mode/xml/xml.js',
         'http://localhost/static/js/codemirror/mode/htmlmixed/htmlmixed.js',
         'http://localhost/static/js/codemirror/mode/../addon/fold/xml-fold.js',
         'http://localhost/static/js/codemirror/mode/../addon/edit/matchtags.js']


def test_codemirror_options(request):
    """Test the codemirror options for mimetype generation."""
    from wte.helpers.frontend import codemirror_options
    assert json.loads(codemirror_options(request, 'text/html', include_mode=True)) ==\
        {'mode': 'text/html',
         'theme': 'default',
         'matchTags': True}
    assert json.loads(codemirror_options(request, 'text/javascript', include_mode=False)) ==\
        {'theme': 'default',
         'lint': True,
         'gutters': ['CodeMirror-lint-markers'],
         'matchBrackets': True}


def test_confirm_action():
    """Tests the :func:`~wte.helpers.frontend.confirm_action` function."""
    from wte.helpers.frontend import confirm_action
    assert json.loads(confirm_action('Test', 'This is a test', 'Cancel', 'Ok')) ==\
        {'title': 'Test',
         'msg': 'This is a test',
         'cancel': {'label': 'Cancel'},
         'ok': {'label': 'Ok'}}
    assert json.loads(confirm_action('Test', 'This is a test',
                                     {'label': 'Cancel'},
                                     {'label': 'Ok'})) ==\
        {'title': 'Test',
         'msg': 'This is a test',
         'cancel': {'label': 'Cancel'},
         'ok': {'label': 'Ok'}}
    assert json.loads(confirm_action('Test', 'This is a test',
                                     {'label': 'Cancel', 'class_': 'secondary'},
                                     {'label': 'Ok', 'class_': 'alert'})) ==\
        {'title': 'Test',
         'msg': 'This is a test',
         'cancel': {'label': 'Cancel', 'class_': 'secondary'},
         'ok': {'label': 'Ok', 'class_': 'alert'}}


def test_confirm_delete():
    """Tests the :func:`~wte.helpers.fronend.confirm_delete` function."""
    from wte.helpers.frontend import confirm_delete
    assert json.loads(confirm_delete('User', 'Test', has_parts=False)) ==\
        {'title': 'Delete this User',
         'msg': 'Please confirm that you wish to delete the User "Test".',
         'cancel': {'label': 'Don\'t delete'},
         'ok': {'label': 'Delete',
                'class_': 'alert'}}
    assert json.loads(confirm_delete('module', 'Test', has_parts=True)) ==\
        {'title': 'Delete this module',
         'msg': 'Please confirm that you wish to delete the module "Test" and all its parts.',
         'cancel': {'label': 'Don\'t delete'},
         'ok': {'label': 'Delete',
                'class_': 'alert'}}


def test_time_string():
    """Test the human readable time-string from :func:`~wte.helpers.frontend.time_string`."""
    from wte.helpers.frontend import time_string
    assert time_string(0, 0, 0, 5) == '5 seconds'
    assert time_string(0, 0, 0, 20) == 'less than 30 seconds'
    assert time_string(0, 0, 0, 40) == 'less than a minute'
    assert time_string(0, 0, 1, 0) == '1 minute'
    assert time_string(0, 0, 2, 0) == '2 minutes'
    assert time_string(0, 0, 2, 30) == '3 minutes'
    assert time_string(0, 1, 0, 0) == '1 hour'
    assert time_string(0, 2, 0, 0) == '2 hours'
    assert time_string(0, 2, 5, 0) == '2 hours and 5 minutes'
    assert time_string(0, 2, 5, 30) == '2 hours and 6 minutes'
    assert time_string(0, 8, 5, 0) == '8 hours'
    assert time_string(0, 8, 25, 0) == '8 and a half hours'
    assert time_string(0, 8, 55, 0) == 'a bit less than 9 hours'
    assert time_string(1, 3, 0, 0) == '1 day and 3 hours'
    assert time_string(2, 3, 0, 0) == '2 days and 3 hours'
    assert time_string(3, 0, 0, 0) == '3 days'
    assert time_string(6, 3, 0, 0) == 'about 6 days'
    assert time_string(6, 14, 0, 0) == 'about 6 and a half days'
    assert time_string(6, 19, 0, 0) == 'a bit less than 7 days'
    assert time_string(18, 0, 0, 0) == 'about 3 weeks'
    assert time_string(70, 0, 0, 0) == 'about 3 months'


def test_readable_timedelta():
    """Tests the :func:`~wte.helpers.frontend.readable_timedelta` function."""
    from wte.helpers.frontend import readable_timedelta
    assert readable_timedelta(datetime(2016, 7, 8) - datetime(2016, 7, 4)) ==\
        'in 4 days'
    assert readable_timedelta(datetime(2016, 7, 4) - datetime(2016, 7, 8)) ==\
        '4 days ago'


def test_split_seconds():
    """Test splitting seconds into days, hours, minutes, and seconds."""
    from wte.helpers.frontend import split_seconds
    assert split_seconds(1) == (0, 0, 0, 1)
    assert split_seconds(61) == (0, 0, 1, 1)
    assert split_seconds(3600) == (0, 1, 0, 0)
    assert split_seconds(4 * 3600 * 24) == (4, 0, 0, 0)


def test_natural_list():
    """Tests the natural list join functionality."""
    from wte.helpers.frontend import natural_list
    assert natural_list([]) == ''
    assert natural_list(['a']) == 'a'
    assert natural_list(['a', 'b']) == 'a & b'
    assert natural_list(['a', 'b', 'c']) == 'a, b & c'
    assert natural_list(['a', 'b', 'c'], '; ', ' and ') == 'a; b and c'


def test_set_list():
    """Tests the set list functionality."""
    from wte.helpers.frontend import set_list
    from wte.util import ordered_counted_set
    assert set_list(ordered_counted_set(['Tree'])) == 'Tree'
    assert set_list(ordered_counted_set(['Tree', 'Flower', 'Tree'])) == 'Trees & Flower'
