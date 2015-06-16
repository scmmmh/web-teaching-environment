*************
Configuration
*************

The configuration file generated in the :doc:`setup` step consists of the
following configuration sections:

.. contents::
   :local:

The configuration file uses the standard .ini format that follows this
structure::

  [section_name]
  
  setting.name = value

Web Teaching Environment configuration
======================================

The settings in this section configure the Web Teaching Environment itself.
To work correctly, they must all be specified within the ``[app:main]``
section of the configuration file.

Application settings
--------------------

**pygments.theme** *(optional)*
  The pygments style to use for source-code highlighting. You can find the
  full list of available Pygments styles here: http://pygments.org/demo/
  
  After changing the style you must run the following command to update the
  styles::
  
    WTE generate-custom-styling <configuration.ini> 
  
  Default: default
**codemirror.theme** *(optional)*
  The CodeMirror theme to use for styling the code editors. You can find the
  full list of available Pygments themes here:
  https://codemirror.net/demo/theme.html
  
  After changing the theme you must run the following command to update the
  styles::
  
    WTE generate-custom-styling <configuration.ini> 
  
  Default: default
**style.settings** 
  Here you can specify a settings SCSS file that can be used to change the
  default settings used to generate the WTE styling. The WTE uses Foundation 5
  and you can find a full list of available settings here:
  http://foundation.zurb.com/docs/
  
  After changing the settings you must run the following command to update the
  styles::
  
    WTE generate-custom-styling <configuration.ini> 
  
**style.overrides** 
  Using the overrides setting you can specify an SCSS file that will be
  included as the last SCSS file when generating the WTE styling. This allows
  you to override any of the default styles if they cannot be configured via
  **style.settings**.
  
  After changing the overrides you must run the following command to update the
  styles::
  
    WTE generate-custom-styling <configuration.ini> 
  

SQLAlchemy database connection string
-------------------------------------

**sqlalchemy.url**
  The SQLAlchemy database connection URL. Consult the
  `SQLAlchemy connection string`_ documentation to find the correct format
  for the database and database library you are using.
  
E-Mail settings
---------------

The E-Mail settings are all optional, but if **email.smtp_host** is not
specified, then the e-mail functionality in the Web Teaching Environment will
not be enabled.

**email.smtp_host** *(optional)*
  The SMTP host to use for sending e-mails. If you do not specify an SMTP host,
  then no-emails will be sent. Instead e-mails will be logged, which can be
  useful in a test environment.
**email.sender** *(optional)*
  The sender address used in all e-mails sent by the Web Teaching Environment.
**email.ssl** *(optional)*
  Whether the connection to the SMTP host should be encrypted.
**email.username** *(optional)*
  The username to use for authenticating with the SMTP host, if required.
**email.password** *(optional)*
  The password to use for authenticating with the SMTP host, if required.
 
Session handling configuration
------------------------------

The settings in this section specify how the user sessions are managed. For
details on the available settings, consult the `beaker documentation`_. In most
cases you will only want to change the *beaker.session.key* setting.

**beaker.session.lock_dir**
  The directory used for locking.
  
  Default: %(here)s/tmp
**beaker.session.type**
  The type of session storage to use. By default uses cookie-based sessions.
  
  Default: cookie
**beaker.session.key**
  The key to use for session access. With cookie-based sessions this is the
  name of the cookie to use.
  
  Default: wte
**beaker.session.encrypt_key**
  Encryption key to use to ensure cookie-based sessions are harder to
  manipulate. The key is automatically and semi-randomly generated when the
  configuration is created.
**beaker.session.validate_key**
  Validation key to use to test that cookie-based sessions have not been
  manipulated. The key is automatically and semi-randomly generated when the
  configuration is created.

Pyramid framework configuration
-------------------------------

The settings in this section are set for a production deployment and should
not be changed in a production environment.

**pyramid.reload_templates**
  Whether to automatically reload HTML templates when they are updated.
  
  Default: false
**pyramid.debug_authorization**
  Whether to provide detailed debug information for the authorization process.
  
  Default: false
**pyramid.debug_notfound**
  Whether to provide detailed debug information for URLs that are not handled
  by the Experiment Support System.
  
  Default: false
**pyramid.debug_routematch**
  Whether to provide detailed debug information on the URL processing
  functions.
  
  Default: false
**pyramid.debug_templates**
  Whether to provide detailed debug information for errors in the HTML
  templates.
  
  Default: false
**pyramid.default_locale_name**
  The default locale to use.
  
  Default: en
**pyramid.includes**
  Any additional components to load on application startup. By default the
  Pyramid Transaction Management component is loaded. For debugging add
  ``pyramid_debugtoolbar`` to this setting. **This will allow arbitrary
  access to everything in the application. Do not include on a production
  system.**
  
  Default: pyramid_tm

Default server configuration
============================

This section configures the default built-in application server, which is
mainly designed for use in development and testing. For production scenarios
consult the :doc:`deployment` documentation. These settings must all be
specified with in the ``[server:main]`` section.

**use**
  The application server entry point to use.
  
  Default: egg:waitress#main
**host**
  The host to listen at for connections.
  
  Default: 0.0.0.0
**port**
  The port to listen at for connections.
  
  Default: 6543

Logging configuration
=====================

The settings in this section are passed on to Python's default logging
configuration engine. Consult the `Python logging documentation`_ for details
on how to adapt the configuration. The settings span a number of sections,
detailed in the `Python logging documentation`_.

.. _`SQLAlchemy connection string`: http://docs.sqlalchemy.org/en/latest/core/engines.html#database-urls
.. _`beaker documentation`: http://beaker.readthedocs.org/en/latest/configuration.html
.. _`pyramid framework documentation`: http://docs.pylonsproject.org/projects/pyramid/en/latest/narr/project.html#development-ini
.. _`Python logging documentation`: http://docs.python.org/2/howto/logging.html#configuring-logging
