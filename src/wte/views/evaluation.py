# -*- coding: utf-8 -*-
u"""
#################################################
:mod:`wte.views.evaluation` -- Evaluation Backend
#################################################

The :mod:`~wte.views.evaluation` module provides the backend functionality for
running user evaluations of the Web Teaching Environment.

Routes are defined in :func:`~wte.views.evaluation.init`.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""

import formencode
import json
import transaction

from pyramid.httpexceptions import (HTTPSeeOther)
from pyramid.view import view_config
from pywebtools.renderer import render
from sqlalchemy import and_

from wte.decorators import (current_user)
from wte.models import (DBSession, User, RequestLog)


def init(config):
    u"""Adds the frontend-specific routes (route name, URL pattern
    handler):

    * ``evaluation.autologin`` -- ``/evaluation/autologin`` --
      :func:`~wte.views.evaluation.autologin`
    * ``evaluation.logging`` -- ``/evaluation/logging`` --
      :func:`~wte.views.evaluation.logging`
    """
    config.add_route('evaluation.autologin', '/evaluation/autologin')
    config.add_route('evaluation.logging', '/evaluation/logging')


class AutoLoginSchema(formencode.Schema):
    u"""The :class:`~wte.views.evaluation.LoginSchema` handles the validation of a
    login request.
    """
    return_to = formencode.validators.UnicodeString(if_missing=None)
    u"""URL to redirect to after a successful login (optional)"""
    email = formencode.validators.Email(not_empty=True)
    u"""E-mail address to log in with"""
    display_name = formencode.validators.UnicodeString(not_empty=True)
    u"""Display name to use for registering a new user"""


@view_config(route_name='evaluation.autologin')
@current_user()
def autologin(request):
    u"""Handles the /evaluation/autologin URL which automatically logs a user
    in or if no user with the given e-mail address exists, creates a new one.
    
    **WARNING** This method is inherently unsafe and must not be deployed in
    a production environment.
    """
    try:
        params = AutoLoginSchema().to_python(request.params)
        dbsession = DBSession()
        user = dbsession.query(User).filter(and_(User.email == params['email'],
                                                 User.password == u'')).first()
        if not user:
            user = User(params['email'], params['display_name'])
            with transaction.manager:
                dbsession.add(user)
            dbsession.add(user)
        request.current_user = user
        request.current_user.logged_in = True
        request.session['uid'] = user.id
        if 'return_to' in request.params and request.params['return_to'] != request.current_route_url():
            raise HTTPSeeOther(request.params['return_to'])
        else:
            raise HTTPSeeOther(request.route_url('root'))
    except formencode.Invalid:
        request.session.flash('Missing autologin parameters', queue='error')
        raise HTTPSeeOther(request.route_url('root'))


@view_config(route_name='evaluation.logging')
@render({'application/json': True})
def logging(request):
    u"""Handles the /evaluation/logging URL. The function does nothing in
    itself. It must be combined with the
    :func:`~wte.views.evaluation.logging_tween_factory`.
    """
    return {'status': 'ok'}


def logging_tween_factory(handler, registry):
    u""""The :func:`~wte.views.evaluation.logging_tween_factory` creates a
    pyramid tween that logs all requests using the
    :class:`~wte.models.RequestLog`.
    """
    def logging_tween(request):
        url = request.path_url[len(request.route_url('root')) - 1:]
        if not url.startswith('/static/'):
            dbsession = DBSession()
            with transaction.manager:
                log = RequestLog(request_uri=url,
                                 params=json.dumps(list(request.params.items())))
                if 'uid' in request.session and dbsession.query(User).filter(User.id == request.session['uid']).first():
                    log.user_id = request.session['uid']
                dbsession.add(log)
        return handler(request)
    return logging_tween
