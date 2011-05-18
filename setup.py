from setuptools import setup, find_packages
import os

version = '1.0a_dev'

long_description = (
    open('README.txt').read()
    + '\n' +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read()
    + '\n' +
    open('CHANGES.txt').read()
    + '\n')

setup(name='templer.zope',
      version=version,
      description="Templer system extensions for zope",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['templer'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'templer.core',
          'templer.buildout',
      ],

      tests_require=[
          'zc.buildout==1.4.3',
          'Cheetah', 
          'PasteScript',
          'templer.core',
          'templer.buildout'],
      test_suite='templer.zope.tests.test_all.test_suite',
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
