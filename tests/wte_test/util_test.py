# -*- coding: utf-8 -*-
"""
##############################
Unit tests for :mod:`wte.util`
##############################

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import asset


def test_version():
    """Test the basic :func:`wte.util.version` number"""
    from wte.util import version
    assert version() == asset.version('WebTeachingEnvironment')


def test_ordered_counted_set():
    """Test the :func:`wte.util.ordered_counted_set` function"""
    from wte.util import ordered_counted_set
    assert ordered_counted_set(['Test']) == [('Test', 1)]
    assert ordered_counted_set(['Test 1', 'Test 2', 'Test 1']) == [('Test 1', 2), ('Test 2', 1)]    
