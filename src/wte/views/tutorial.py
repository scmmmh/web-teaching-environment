# -*- coding: utf-8 -*-
u"""

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import transaction
import formencode

from pyramid.httpexceptions import (HTTPSeeOther, HTTPNotFound)
from pyramid.view import view_config
from pywebtools.renderer import render
from pywebtools.auth import is_authorised
from sqlalchemy import and_

from wte.decorators import current_user
from wte.util import (unauthorised_redirect, State, send_email, get_config_setting)
from wte.models import (DBSession, Module, Tutorial)

def init(config):
    config.add_route('tutorial.new', '/modules/{mid}/tutorials/new')
    config.add_route('tutorial.edit', '/modules/{mid}/tutorials/{tid}/edit')
    config.add_route('tutorial.delete', '/modules/{mid}/tutorials/{tid}/delete')

class TutorialSchema(formencode.Schema):
    u"""The :class:`~wte.views.backend.NewModuleSchema` handles the validation
    of a new :class:`~wte.models.Tutorial`.
    """
    title = formencode.validators.UnicodeString(not_empty=True)
    u"""The module's title"""
    status = formencode.All(formencode.validators.UnicodeString(not_empty=True),
                            formencode.validators.OneOf([u'unavailable',
                                                         u'available']))
    u"""The module's status"""
    page_id = formencode.foreach.ForEach(formencode.validators.Int())
    u"""The ids of the child pages"""
    
@view_config(route_name='tutorial.new')
@render({'text/html': 'tutorial/new.html'})
@current_user()
def new(request):
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict['mid']).first()
    if module:
        if is_authorised(u':module.allow("edit" :current)', {'module': module,
                                                             'current': request.current_user}):
            if request.method == u'POST':
                try:
                    params = TutorialSchema().to_python(request.params)
                    dbsession = DBSession()
                    with transaction.manager:
                        dbsession.add(module)
                        max_order = [t.order + 1 for t in module.tutorials]
                        max_order.append(0)
                        max_order = max(max_order)
                        
                        new_tutorial = Tutorial(title=params['title'],
                                                status=params['status'],
                                                module=module,
                                                order=max_order)
                        dbsession.add(new_tutorial)
                    dbsession.add(new_tutorial)
                    request.session.flash('Your new tutorial has been created', queue='info')
                    raise HTTPSeeOther(request.route_url('tutorial.view', mid=request.matchdict['mid'], tid=new_tutorial.id))
                except formencode.Invalid as e:
                    e.params = request.params
                    return {'e': e,
                            'module': module,
                            'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                                       {'title': module.title, 'url': request.route_url('module.view', mid=module.id)},
                                       {'title': 'Add Tutorial', 'url': request.route_url('tutorial.new', mid=module.id), 'current': True}]}
            return {'module': module,
                    'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                               {'title': module.title, 'url': request.route_url('module.view', mid=module.id)},
                               {'title': 'Add Tutorial', 'url': request.route_url('tutorial.new', mid=module.id), 'current': True}]}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()

@view_config(route_name='tutorial.edit')
@render({'text/html': 'tutorial/edit.html'})
@current_user()
def edit(request):
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict['mid']).first()
    tutorial = dbsession.query(Tutorial).filter(and_(Tutorial.id==request.matchdict['tid'],
                                                     Tutorial.module_id==request.matchdict['mid'])).first()
    if module and tutorial:
        if is_authorised(u':module.allow("edit" :current)', {'module': module,
                                                             'current': request.current_user}):
            if request.method == u'POST':
                try:
                    params = TutorialSchema().to_python(request.params)
                    with transaction.manager:
                        dbsession.add(tutorial)
                        tutorial.title = params['title']
                        tutorial.status = params['status']
                        if params['page_id']:
                            for order, pid in enumerate(params['page_id']):
                                for page in tutorial.pages:
                                    if page.id == int(pid):
                                        dbsession.add(page)
                                        page.order = order
                    request.session.flash('The tutorial has been updated', queue='info')
                    raise HTTPSeeOther(request.route_url('tutorial.view', mid=request.matchdict['mid'], tid=request.matchdict['tid']))
                except formencode.Invalid as e:
                    e.params = params
                    return {'e': e,
                            'module': module,
                            'tutorial': tutorial,
                            'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                                       {'title': module.title, 'url': request.route_url('module.view', mid=module.id)},
                                       {'title': tutorial.title, 'url': request.route_url('tutorial.view', mid=module.id, tid=tutorial.id)},
                                       {'title': 'Edit', 'url': request.route_url('tutorial.edit', mid=module.id, tid=tutorial.id), 'current': True}]}
            return {'module': module,
                    'tutorial': tutorial,
                    'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                               {'title': module.title, 'url': request.route_url('module.view', mid=module.id)},
                               {'title': tutorial.title, 'url': request.route_url('tutorial.view', mid=module.id, tid=tutorial.id)},
                               {'title': 'Edit', 'url': request.route_url('tutorial.edit', mid=module.id, tid=tutorial.id), 'current': True}]}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()

@view_config(route_name='tutorial.delete')
@render({'text/html': 'tutorial/delete.html'})
@current_user()
def delete(request):
    dbsession = DBSession()
    module = dbsession.query(Module).filter(Module.id==request.matchdict['mid']).first()
    tutorial = dbsession.query(Tutorial).filter(and_(Tutorial.id==request.matchdict['tid'],
                                                     Tutorial.module_id==request.matchdict['mid'])).first()
    if module and tutorial:
        if is_authorised(u':module.allow("edit" :current)', {'module': module,
                                                             'current': request.current_user}):
            if request.method == u'POST':
                with transaction.manager:
                    dbsession.delete(tutorial)
                request.session.flash('The tutorial has been deleted', queue='info')
                raise HTTPSeeOther(request.route_url('module.view', mid=request.matchdict['mid']))
            return {'module': module,
                    'tutorial': tutorial,
                    'crumbs': [{'title': 'Modules', 'url': request.route_url('modules')},
                               {'title': module.title, 'url': request.route_url('module.view', mid=module.id)},
                               {'title': tutorial.title, 'url': request.route_url('tutorial.view', mid=module.id, tid=tutorial.id)},
                               {'title': 'Delete', 'url': request.route_url('tutorial.delete', mid=module.id, tid=tutorial.id), 'current': True}]}
        else:
            unauthorised_redirect(request)
    else:
        raise HTTPNotFound()
