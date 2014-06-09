# -*- coding: utf-8 -*-
u"""
###################################################
:mod:`wte.views.frontend` -- Frontend view handlers
###################################################

The :mod:`~wte.views.frontend` handles the frontend functionality for
interacting with :class:`~wte.models.Module`, :class:`~wte.models.Part`, and
:class:`~wte.models.Page`.

Routes are defined in :func:`~wte.views.frontend.init`.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import transaction

from pyramid.httpexceptions import (HTTPNotFound)
from pyramid.response import Response
from pyramid.view import view_config
from pywebtools.auth import is_authorised
from pywebtools.renderer import render
from sqlalchemy import and_

from wte.decorators import current_user
from wte.models import (DBSession, Module, Part, User, UserPartProgress,
                        File)
from wte.util import (unauthorised_redirect)


def init(config):
    u"""Adds the frontend-specific backend routes (route name, URL pattern
    handler):
    
    * ``modules`` -- ``/modules`` -- :func:`~wte.views.frontend.modules`
    * ``module.view`` -- ``/modules/{mid}`` --
      :func:`~wte.views.frontend.view_module`
    * ``tutorial.view`` -- ``/modules/{mid}/tutorials/{tid}`` --
      :func:`~wte.views.frontend.view_tutorial`
    * ``exercise.view`` -- ``/modules/{mid}/exercises/{eid}`` --
      :func:`~wte.views.frontend.view_exercise`
    * ``page.view`` -- ``/modules/{mid}/tutorials/{tid}/pages/{pid}`` --
      :func:`~wte.views.frontend.view_page`
    * ``user.modules`` -- ``/users/{uid}/modules`` --
      :func:`~wte.views.frontend.user_modules`
    * ``file.view`` -- ``/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/name/{filename}``
      -- :func:`~wte.views.frontend.view_file`
    * ``file.save`` -- ``/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/id/{fid}/save``
      -- :func:`~wte.views.frontend.save_file`
    """
    config.add_route('modules', '/modules')
    config.add_route('module.view', '/modules/{mid}')
    config.add_route('part.view', '/modules/{mid}/parts/{pid}')
    config.add_route('tutorial.view', '/modules/{mid}/tutorials/{tid}')
    config.add_route('exercise.view', '/modules/{mid}/exercises/{eid}')
    config.add_route('page.view', '/modules/{mid}/tutorials/{tid}/pages/{pid}')
    config.add_route('user.modules', '/users/{uid}/modules')
    config.add_route('file.view', '/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/name/{filename}')
    config.add_route('file.save', '/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/id/{fid}/save')


@view_config(route_name='modules')
@render({'text/html': 'module/list.html'})
@current_user()
def modules(request):
    u"""Handles the ``/modules`` URL, displaying all available
    :class:`~wte.models.Module`.
    """
    dbsession = DBSession()
    modules = dbsession.query(Module).filter(Module.status==u'available').all()
    return {'modules': modules,
            'crumbs': [{'title': 'Modules', 'url': request.route_url('modules'), 'current': True}]}


@view_config(route_name='user.modules')
@render({'text/html': 'module/user.html'})
@current_user()
def user_modules(request):
    u"""Handles the ``/users/{uid}/modules`` URL, displaying all the
    :class:`~wte.models.Module` of the :class:`~wte.models.User`.
    
    Requires that the current user has "view" rights for the
    :class:`~wte.models.User`.
    """
    dbsession = DBSession()
    user = dbsession.query(User).filter(User.id==request.matchdict['uid']).first()
    if user:
        if user.allow('view', request.current_user):
            return {'user': user,
                    'crumbs': [{'title': user.display_name, 'url': request.route_url('user.view', uid=user.id)},
                               {'title': 'Modules', 'url': request.route_url('modules'), 'current': True}]}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()


@view_config(route_name='module.view')
@render({'text/html': 'module/view.html'})
@current_user()
def view_module(request):
    u"""Handles the ``/modules/{mid}`` URL, displaying the
    :class:`~wte.models.Module` and its child :class:`~wte.models.Part`.
    
    Requires that the user has "view" rights on the
    :class:`~wte.models.Module`.
    """
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict['mid']).first()
    if module:
        if is_authorised(u':module.allow("view" :current)', {'module': module,
                                                             'current': request.current_user}):
            return {'module': module,
                    'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                               {'title': module.title, 'url': request.route_url('module.view', mid=module.id), 'current': True}]}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()


def get_user_part_progress(dbsession, user, part, page=None):
    u"""Returns the :class:`~wte.models.UserPartProgress` for the given
    ``user`` and ``part. If none exists, then a new one is instantiated. If
    the :class:`~wte.models.UserPartProgress` points to a current page that
    is different to ``page``, then the :class:`~wte.models.UserPartProgress`
    is updated.
    
    :param user: The user to get the progress for
    :type user: :class:`~wte.models.User`
    :param part: The part to get the progress for
    :type part: :class:`~wte.models.Part`
    :return: The :class:`~wte.models.UserPartProgress`
    :rtype: :class:`~wte.models.UserPartProgress`
    """
    user_part = None
    for part_asc in user.parts:
        if part_asc.part == part:
            user_part = part_asc
            break
    if not user_part:
        with transaction.manager:
            dbsession.add(part)
            user_part = UserPartProgress(user=user,
                                         part=part,
                                         current_page=page)
            for template in part.templates:
                user_part.files.append(File(order=template.order,
                                            filename=template.filename,
                                            mimetype=template.mimetype,
                                            content=template.content))
            dbsession.add(user_part)
    elif page:
        if user_part.page_id != page.id:
            with transaction.manager:
                dbsession.add(page)
                dbsession.add(user_part)
                user_part.current_page = page
    return user_part


@view_config(route_name='part.view')
@render({'text/html': 'part/view.html'})
@current_user()
def view_part(request):
    u"""Handles the ``/modules/{mid}/parts/{pid}`` URL, displaying the
    :class:`~wte.models.Part`.
    
    Requires that the user has "view" rights on the
    :class:`~wte.models.Part`.
    """
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id == request.matchdict['mid']).first()
    part = dbsession.query(Part).filter(and_(Part.id == request.matchdict['pid'],
                                             Part.module_id==request.matchdict['mid'])).first()
    if module and part:
        if part.allow('view', request.current_user):
            progress = dbsession.query(UserPartProgress).\
                filter(and_(UserPartProgress.user_id == request.current_user.id,
                            UserPartProgress.part_id == request.matchdict['pid'])).first()
            if not progress:
                if part.type == u'tutorial':
                    pass
                elif part.type == u'page':
                    pass
                elif part.type == u'exercise':
                    pass
                elif part.type == u'task':
                    pass
            if progress:
                with transaction.manager:
                    dbsession.add(progress)
            crumbs = [{'title': 'Modules', 'url': request.route_url('modules')},
                      {'title': module.title, 'url': request.route_url('module.view', mid=module.id)}]
            tmp = part
            while tmp:
                crumbs.insert(2, {'title': tmp.title, 'url': request.route_url('part.view', mid=module.id, pid=tmp.id)})
                tmp = tmp.parent
            crumbs[-1]['current'] = True
            return {'module': module,
                    'part': part,
                    'crumbs': crumbs,
                    'progress': progress}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()


@view_config(route_name='file.view')
@current_user()
def view_file(request):
    u"""Handles the ``/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/name/{filename}``
    URL, sending back the correct :class:`~wte.models.File`.
    
    Requires that the user has "view" rights on the
    :class:`~wte.models.Module`. It will also only send a
    :class:`~wte.models.File` belonging to the current
    :class:`~wte.models.User`.
    """
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict[u'mid']).first()
    part = dbsession.query(Part).filter(and_(Part.id==request.matchdict[u'ptid'],
                                             Part.module_id==request.matchdict[u'mid'])).first()
    if request.matchdict[u'pid'] == 'exercise':
        page = None
    else:
        page = dbsession.query(Page).filter(and_(Page.id==request.matchdict[u'pid'],
                                                 Page.part_id==request.matchdict[u'ptid'])).first()
    if module and part:
        if part.allow('view', request.current_user):
            progress = get_user_part_progress(dbsession, request.current_user, part, page)
            dbsession.add(progress)
            for user_file in progress.files:
                if user_file.filename == request.matchdict['filename']:
                    return Response(body=user_file.content,
                                    headerlist=[('Content-Type', str(user_file.mimetype))])
            raise HTTPNotFound()
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()

@view_config(route_name='file.save')
@render({'application/json': True})
@current_user()
def save_file(request):
    u"""Handles the ``/modules/{mid}/parts/{ptid}/pages/{pid}/users/{uid}/files/id/{fid}/save``
    URL, updating the :class:`~wte.models.File` content.
    
    Requires that the user has "view" rights on the
    :class:`~wte.models.Module`. It will also only send a
    :class:`~wte.models.File` belonging to the current
    :class:`~wte.models.User`.
    """
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict[u'mid']).first()
    part = dbsession.query(Part).filter(and_(Part.id==request.matchdict[u'ptid'],
                                             Part.module_id==request.matchdict[u'mid'])).first()
    if request.matchdict[u'pid'] == 'exercise':
        page = None
    else:
        page = dbsession.query(Page).filter(and_(Page.id==request.matchdict[u'pid'],
                                                 Page.part_id==request.matchdict[u'ptid'])).first()
    if module and part:
        if part.allow('view', request.current_user):
            progress = get_user_part_progress(dbsession, request.current_user, part, page)
            dbsession.add(progress)
            for user_file in progress.files:
                if user_file.id == int(request.matchdict['fid']):
                    if 'content' in request.params:
                        with transaction.manager:
                            dbsession.add(user_file)
                            user_file.content = request.params['content']
                        return {'status': 'saved'}
                    else:
                        return {'status': 'no-changes'}
            raise HTTPNotFound()
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()
