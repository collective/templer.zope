.. contents::

Introduction
============

This package extends the functionality of the templer code generation system.
It builds upon the functionality of templer.core_ and templer.buildout_, and
depends on those packages. This package provides basic support for creating
zope packages and zope buildouts. Included are packages for basic zope
packages and basic zope buildouts.

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _templer.buildout: http://pypi.python.org/pypi/templer.buildout

Creating Packages
-----------------

As with the parent package, templer.core, creating packages using
templer.zope templates is accomplished by using the ``templer`` script. The
script is invoked thus::

    templer zope2_basic

This will create a basic zope package skeleton.

Provided Templates
------------------

This package provides two templates for Zope package development

zope2_basic
    A namespace package for developing Zope2 applications.  The package comes
    complete with a simple development buildout for Zope2 in which the package
    is installed

zope2_nested
    A nested namespace package for developing Zope2 applications.  The package
    comes complete with a simple development buildout for Zope2 in which the
    package is installed

Other Functions
---------------

The ``templer`` script provides a number of other functions, these are 
described in full on the index page for templer.core_ at PyPI_

.. _templer.core: http://pypi.python.org/pypi/templer.core
.. _PyPI: http://pypi.python.org/pypi
