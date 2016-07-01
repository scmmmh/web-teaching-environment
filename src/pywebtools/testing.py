# -*- coding: utf-8 -*-
"""
############################################
:mod:`pywebtools.testing` -- py.test plugins
############################################

The primary use point is the :func:`~pywebtools.testing.functional_tester`
fixture.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
from __future__ import (absolute_import, division, print_function, unicode_literals)

import pytest
import transaction

from alembic import config, command
from pkg_resources import resource_stream
from pyramid.paster import (get_app, get_appsettings, setup_logging)
from pywebtools.sqlalchemy import DBSession, Base
from pywebtools.pyramid.auth.models import User, PermissionGroup, Permission
from sqlalchemy import engine_from_config
from webtest import TestApp

from wte import models

dbsession_initialised = False


@pytest.yield_fixture
def database():
    """The :func:`~pywebtools.testing.database` fixture initialises the database specified
    in the "testing.ini", removes any existing data, creates the standard permissions, and
    four test users:

    * admin - user with full administrative permissions
    * developer - user with full experiment development permissions
    * content - user with full editing permissions
    * general - user with no permissions
    """
    global dbsession_initialised

    # Load settings
    settings = get_appsettings('testing.ini')
    setup_logging('testing.ini')

    # Init the DB
    engine = engine_from_config(settings, 'sqlalchemy.')
    if not dbsession_initialised:
        DBSession.configure(bind=engine)
        dbsession_initialised = True
    Base.metadata.create_all(engine)

    dbsession = DBSession()

    # Reset Database Content
    with transaction.manager:
        tables = list(Base.metadata.sorted_tables)
        tables.reverse()
        for table in tables:
            dbsession.bind.execute(table.delete())
        dbsession.flush()

    # Create Test Users
    with transaction.manager:
        admin_user = User(email='admin@example.com',
                          display_name='Admin')
        admin_user.new_password('password')
        developer_user = User(email='developer@example.com',
                              display_name='Developer')
        developer_user.new_password('password')
        content_user = User(email='content@example.com',
                            display_name='Content')
        content_user.new_password('password')
        general_user = User(email='general@example.com',
                            display_name='General')
        general_user.new_password('password')
        dbsession.add(general_user)
        group = PermissionGroup(title='Site administrator')
        group.permissions.append(Permission(name='admin.users', title='Administer the users'))
        group.permissions.append(Permission(name='admin.groups', title='Administer the permission groups'))
        group.permissions.append(Permission(name='admin.question_types', title='Administer the question types'))
        admin_user.permission_groups.append(group)
        group = PermissionGroup(title='Developer')
        group.permissions.append(Permission(name='survey.new', title='Create new experiments'))
        admin_user.permission_groups.append(group)
        developer_user.permission_groups.append(group)
        group = PermissionGroup(title='Content administrator')
        group.permissions.append(Permission(name='survey.view-all', title='View all experiments'))
        group.permissions.append(Permission(name='survey.edit-all', title='Edit all experiments'))
        group.permissions.append(Permission(name='survey.delete-all', title='Delete all experiments'))
        content_user.permission_groups.append(group)
        dbsession.add(admin_user)
        dbsession.add(developer_user)
        dbsession.add(content_user)

    # Alembic Stamp
    alembic_config = config.Config('testing.ini', ini_section='app:main')
    alembic_config.set_section_option('app:main', 'script_location', 'wte:migrations')
    command.stamp(alembic_config, "head")

    DBSession.remove()

    yield DBSession


@pytest.yield_fixture
def app(database):
    """Fixture that provides a newly initialised pyramid application defined in "testing.ini"
    with an empty database.
    """
    # Create the application
    app = get_app('testing.ini')

    # Yield to the test
    yield app


class RequestTesterMixin(object):
    """The :class:`~pywebtools.testing.RequestTesterMixin` provides functionality for making requests
    via the :class:`~pywebtools.testing.FunctionalTester`.
    """

    def get_url(self, url, headers=None):
        """Send a GET request to the given ``url``.

        :param url: The url to request
        :type url: ``unicode``
        :param headers: Optional headers to send with the request
        :type headers: ``dict`` or ``list``
        """
        if headers:
            if isinstance(headers, dict):
                if 'Accept' not in headers:
                    headers['Accept'] = '*/*'
            elif isinstance(headers, list):
                if 'Accept' not in dict(headers):
                    headers.append(('Accept', '*/*'))
        else:
            headers = [('Accept', '*/*')]
        self._response = self._test.get(url, headers=headers, status='*')

    def has_text(self, text):
        """Check whether the last response contains the given ``text``.

        :param text: The text to look for
        :type text: ``unicode``
        """
        if self._response:
            assert text in self._response.body.decode('utf-8')
        else:
            assert False, 'No request sent'

    def has_status(self, status):
        if self._response:
            assert self._response.status_int == status,\
            'Response status is %s instead of %s' % (self._response.status_int, status)
        else:
            assert False, 'No request sent'


class DBTesterMixin(object):
    """The :class:`~pywebtools.testing.DBTesterMixin` provides functionality for interacting with the
    database via the :class:`~pywebtools.testing.FunctionalTester`.
    """

    def __init__(self):
        self._dbsession = DBSession()

    def get_model(self, name, query):
        """Retrieve a single instance of the model ``name``, filtered by the ``query``.

        :param name: The name of the model to get the instance for
        :type name: ``unicode``
        :param query: The query to use for selecting the instance
        :type query: ``unicode``
        :return: The result of the query
        """
        cls = getattr(models, name)
        return self._dbsession.query(cls).filter(query).first()

    def create_model(self, name, params):
        """Create a new instance of the model ``name`` with the given ``params``.

        :param name: The name of the model to create the instance of
        :type name: ``unicode``
        :param params: The initial parameters to use for creating the instance
        :type params: ``dict``
        :return: The new instance
        """
        cls = getattr(models, name)
        with transaction.manager:
            model = cls(**params)
            self._dbsession.add(model)
        self._dbsession.add(model)
        return model


class FunctionalTester(RequestTesterMixin, DBTesterMixin):
    """The :class:`~pywebtools.testing.FunctionalTester` provides an easy interface for running
    functional tests. It mixes in :class:`~pywebtools.testing.RequestTesterMixin` and
    :class:`~pywebtools.testing.DBTesterMixin` to provide the actual functionality.

    The :class:`~pywebtools.testing.FunctionalTester` should always be created via the
    :func:`~pywebtools.testing.functional_tester` fixture.
    """

    def __init__(self, app):
        self._app = app
        self._test = TestApp(app)
        self._response = None
        DBTesterMixin.__init__(self)


@pytest.yield_fixture
def functional_tester(app, database):
    """Fixture that provides a :class:`~pywebtools.testing.FunctionalTester`.
    """
    tester = FunctionalTester(app)
    yield tester
