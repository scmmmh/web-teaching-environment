# -*- coding: utf-8 -*-
"""
####################################################
:mod:`wte.helpers` -- Helper functionality for views
####################################################

The :mod:`~wte.helpers` module imports various helper modules that can be used
in the templates via the ``h`` variable. For details of the functions available
consulte the following documentation: :mod:`pywebtools.text`,
:mod:`wte.helpers.auth`, and :mod:`wte.helpers.form`.

.. moduleauthor:: Mark Hall <mark.hall@work.room3b.eu>
"""
import asset

from . import frontend  # NOQA


def version():
    """Return the current version number."""
    return asset.version('WebTeachingEnvironment')
