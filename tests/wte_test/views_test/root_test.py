# -*- coding: utf-8 -*-
"""
#####################################
Functional Tests for :mod:`wte.views`
#####################################

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""


def test_root(functional_tester):
    """Tests the root view."""
    functional_tester.get_url('/')
    functional_tester.has_text('Web Teaching Environment')


def test_help(functional_tester):
    """Tests an explicit help page."""
    functional_tester.get_url('/help/index.html')
    functional_tester.has_text('Web Teaching Environment')
    functional_tester.has_text('Documentation')


def test_help_default(functional_tester):
    """Tests accessing a default help page."""
    functional_tester.get_url('/help/')
    functional_tester.has_text('Web Teaching Environment')
    functional_tester.has_text('Documentation')


def test_help_missing(functional_tester):
    """Tests accessing a missing help page."""
    functional_tester.get_url('/help/this-does-not-exist')
    functional_tester.has_status(404)
    functional_tester.has_text('Not Found')


def test_404(functional_tester):
    """Tests accessing a missing page."""
    functional_tester.get_url('/this-does-not-exist')
    functional_tester.has_status(404)
    functional_tester.has_text('Not Found')


def test_500(functional_tester):
    """Tests that server errors give a 500 error."""
    functional_tester.get_url('/users/invalid-id')
    functional_tester.has_status(500)
