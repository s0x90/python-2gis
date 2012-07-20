# -*- coding: utf-8 -*-

"""
python-2gis
============

A Python library for accessing the 2gis API
"""

from setuptools import setup, find_packages

from dgis import __version__

setup(
    name='dgis',
    version=__version__,
    author='SvartalF',
    author_email='self@svartalf.info',
    url='https://github.com/svartalf/python-2gis',
    description='2gis library for Python',
    long_description=__doc__,
    packages=find_packages(),
    classifiers=(
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries',
    ),
)