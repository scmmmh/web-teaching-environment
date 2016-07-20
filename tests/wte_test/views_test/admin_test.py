# -*- coding: utf-8 -*-
"""
###########################################
Functional Tests for :mod:`wte.views.admin`
###########################################

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""


def test_admin_no_auth(functional_tester):
    functional_tester.get_url('/admin')
    functional_tester.has_text('users/login')
