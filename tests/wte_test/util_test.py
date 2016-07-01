# -*- coding: utf-8 -*-
u"""
##############################
Unit tests for :mod:`wte.util`
##############################

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
from nose.tools import eq_, ok_


def version_test():
    u"""Test the basic :data:`wte.util.VERSION` number"""
    from wte.util import version

    eq_('str', version().__class__.__name__)


def state_object_test():
    u"""Test the generic :class:`wte.util.State` object"""
    from wte.util import State

    state = State()
    ok_(state)
    state = State(setting='value')
    ok_(state.setting)
    eq_('value', state.setting)


def unauthorised_redirect_to_login_test():
    u"""Test that :func:`wte.util.unauthorised_redirect` redirects to
    the login page."""
    ok_(False, 'Must not reach this line')


def unauthorised_redirect_to_login_with_message_test():
    u"""Test that :func:`wte.util.unauthorised_redirect` redirects to
    the login page with a custom message."""
    ok_(False, 'Must not reach this line')


def unauthorised_redirect_to_root_test():
    u"""Test that :func:`wte.util.unauthorised_redirect` redirects to
    the root page for logged-in users."""
    ok_(False, 'Must not reach this line')


def unauthorised_redirect_to_root_with_message_test():
    u"""Test that :func:`wte.util.unauthorised_redirect` redirects to
    the root page for logged-in users with a custom message."""
    ok_(False, 'Must not reach this line')


def unauthorised_redirect_to_location_test():
    u"""Test that :func:`wte.util.unauthorised_redirect` redirects to
    a custom page for logged-in users."""
    ok_(False, 'Must not reach this line')


def send_email_no_config_test():
    u"""Tests that :func:`wte.util.send_email` works if no "email.smtp_host"
    is set."""
    ok_(False, 'Must not reach this line')


def send_email_fail_test():
    u"""Tests that :func:`wte.util.send_email` works when an invalid "email.smtp_host"
    is set."""
    ok_(False, 'Must not reach this line')


def convert_type_test():
    u"""Tests the basic conversion using :func:`wte.util.convert_type`."""
    from wte.util import convert_type

    eq_('input', convert_type('input', 'string'))
    eq_(None, convert_type(None, 'string', default=None))
    eq_('default', convert_type(None, 'string', default='default'))


def convert_type_int_test():
    u"""Tests integer conversion using :func:`wte.util.convert_type`."""
    from wte.util import convert_type

    eq_(1, convert_type('1', 'int'))
    eq_(None, convert_type('a', 'int'))
    eq_(0, convert_type('a', 'int', default=0))


def convert_type_bool_test():
    u"""Tests boolean conversion using :func:`wte.util.convert_type`."""
    from wte.util import convert_type

    eq_(True, convert_type('true', 'boolean'))
    eq_(True, convert_type('True', 'boolean'))
    eq_(False, convert_type('false', 'boolean'))
    eq_(False, convert_type('False', 'boolean'))


def get_config_setting_test():
    u"""Tests getting configuration settings using
    :func:`wte.util.get_config_setting`."""
    ok_(False, 'Must not reach this line')
