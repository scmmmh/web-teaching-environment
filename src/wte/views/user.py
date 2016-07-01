# -*- coding: utf-8 -*-
"""
#########################################################
:mod:`wte.views.user` -- User functionality view handlers
#########################################################

The :mod:`~wte.views.user` module handles all user functionality.

Routes are defined in :func:`~wte.views.user.init`.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
from pywebtools.pyramid import auth as pyramid_auth

from wte.util import (send_email, get_config_setting)


def init(config):
    """Adds the user-specific routes (route name, URL pattern, handler):

    * ``users`` -- ``/users`` -- :func:`~wte.views.user.users`
    * ``users.action`` -- ``/users/action`` -- :func:`~wte.views.user.action`
    * ``user.view`` -- ``/users/{uid}`` -- :func:`~wte.views.user.view`
    * ``user.edit`` -- ``/users/{uid}/edit`` -- :func:`~wte.views.user.edit`
    * ``user.permissions`` -- ``/users/{uid}/permissions`` --
      :func:`~wte.views.user.permissions`
    * ``user.delete`` -- ``/users/{uid}/delete`` --
      :func:`~wte.views.user.delete`

    Also initialises the :mod:`pywebtools.pyramid.auth` authentication system
    """
    pyramid_auth.init(config,
                      renderers={'user.login': 'wte:templates/users/login.kajiki',
                                 'user.logout': 'wte:templates/users/logout.kajiki',
                                 'user.register': 'wte:templates/users/register.kajiki',
                                 'user.confirm': 'wte:templates/users/confirm.kajiki',
                                 'user.forgotten_password': 'wte:templates/users/forgotten_password.kajiki',
                                 'user.reset_password': 'wte:templates/users/reset_password.kajiki',
                                 'users': 'wte:templates/users/list.kajiki',
                                 'users.action': 'wte:templates/users/action.kajiki',
                                 'user.view': 'wte:templates/users/view.kajiki',
                                 'user.edit': 'wte:templates/users/edit.kajiki',
                                 'user.permissions': 'wte:templates/users/permissions.kajiki',
                                 'user.delete': 'wte:templates/users/delete.kajiki'},
                      redirects={'_default': 'root',
                                 'user.login': {'route': 'part.list',
                                                'params': {'_query': {'user_id': '{uid}'}}},
                                 'user.logout': 'root',
                                 'user.register': 'root',
                                 'user.forgotten_password': 'root',
                                 'user.reset_password': {'route': 'part.list',
                                                         'params': {'_query': {'user_id': '{uid}'}}}},
                      callbacks={'user.created': new_user_created,
                                 'user.validated': new_user_validated,
                                 'user.password_reset': password_reset,
                                 'user.password_reset_failed': password_reset_failed,
                                 'user.password_reset_complete': password_reset_complete})


def new_user_created(request, user, token):
    """Callback that sends an e-mail to the newly created user's e-mail address
    to give them a validation link.

    :param request: The request to use for configuration settings
    :type request: :class:`~pyramid.request.Request`
    :param user: The user to send the e-mail to
    :type user: :class:`~pywebtools.pyramid.auth.models.User`
    :param token: The validation token
    :type token: :class:`~pywebtools.pyramid.auth.models.TimeToken`
    """
    request.session.flash('A confirmation e-mail has been sent to the e-mail address you provided.', queue='info')
    send_email(request,
               user.email,
               get_config_setting(request, 'email.sender',
                                  default='no-reply@example.com'),
               'Please confirm your registration',
               '''Hello %s,

Thank you for registering with the Web Teaching Environment. To complete your
registration, please click on the following link or copy it into your browser:

%s

This link is valid for 60 minutes. If you do not confirm your registration within
that time, you will need to use the "Forgotten Password" function to request a new
confirmation link.

Best Regards,
Web Teaching Environment''' % (user.display_name,
                               request.route_url('user.confirm',
                                                 token=token.token)))


def new_user_validated(request, user, token):
    """Callback that sends an e-mail to the newly created user's e-mail address
    to give them a password-reset link.

    :param request: The request to use for configuration settings
    :type request: :class:`~pyramid.request.Request`
    :param user: The user to send the e-mail to
    :type user: :class:`~pywebtools.pyramid.auth.models.User`
    :param token: The validation token
    :type token: :class:`~pywebtools.pyramid.auth.models.TimeToken`
    """
    send_email(request,
               user.email,
               get_config_setting(request, 'email.sender',
                                  default='no-reply@example.com'),
               'Registration for the Web Teaching Environment Complete',
               '''Hello %s,

Thank you for completing the registration process. To log in, please
click on the following link and set a new password:

%s

The link is valid for 20 minutes. If you do not set a password within that time,
you will need to use the "Forgotten Password" function to request a new confirmation
link.

Best Regards,
Web Teaching Environment''' % (user.display_name, request.route_url('user.reset_password', token=token.token)))


def password_reset(request, user, token):
    """Callback that sends an e-mail to the user's e-mail address with a
    link to reset their password.

    :param request: The request to use for configuration settings
    :type request: :class:`~pyramid.request.Request`
    :param user: The user to send the e-mail to
    :type user: :class:`~pywebtools.pyramid.auth.models.User`
    """
    request.session.flash('A password reset link has been sent to the e-mail address you provided.', queue='info')
    send_email(request,
               user.email,
               get_config_setting(request, 'email.sender',
                                  default='no-reply@example.com'),
               'Password for the Web Teaching Environment reset',
               '''Hello %s,

You have asked to have your password reset. To complete the reset password
click on the following link or copy it into your browser:

%s

The link is valid for 20 minutes. If you do not set a password within that time,
you will need to use the "Forgotten Password" function to request a new confirmation
link.

If you did not ask for your password to be reset, then please check that
nobody else has access to your e-mail account and might be trying to
access your Web Teaching Environment account.

Best Regards,
Web Teaching Environment''' % (user.display_name, request.route_url('user.reset_password', token=token.token)))


def password_reset_failed(request):
    """Callback that handles a failed password reset."""
    request.session.flash('A password reset link has been sent to the e-mail address you provided.', queue='info')


def password_reset_complete(request, user):
    """Callback that sends an e-mail to the user's e-mail address letting them
    know that their password has been reset.

    :param request: The request to use for configuration settings
    :type request: :class:`~pyramid.request.Request`
    :param user: The user to send the e-mail to
    :type user: :class:`~pywebtools.pyramid.auth.models.User`
    """
    send_email(request,
               user.email,
               get_config_setting(request, 'email.sender',
                                  default='no-reply@example.com'),
               'Reset your password for the Web Teaching Environment',
               '''Hello %s,

You have just reset your password for the Web Teaching Environment.

If you have not done so, then please contact your administrator as soon as
possible as somebody else may have gained access to your account.

Best Regards,
Web Teaching Environment''' % user.display_name)
