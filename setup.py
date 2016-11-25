#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: wuyue92tree@163.com

from os.path import dirname, join
from setuptools import setup, find_packages

with open(join(dirname(__file__), 'crwyadmin/VERSION'), 'rb') as f:
    version = f.read().decode('ascii').strip()

setup(
    name='django-crwyadmin',
    version=version,
    url='https://github.com/wuyue92tree/django-crwyadmin',
    description='django admin by adminlte',
    long_description=open('README.rst').read(),
    author='wuyue',
    author_email='wuyue92tree@163.com',
    maintainer='wuyue',
    maintainer_email='wuyue92tree@163.com',
    license='BSD',
    packages=find_packages(exclude=('tmpadmin', 'tmpadmin.*')),
    include_package_data=True,
    zip_safe=False,
    entry_points={
    },
    install_requires=[
        'Django >= 1.10.3',
        'django-braces >= 1.9.0',
    ], )
