#!/usr/bin/env python

import os
from sys import version_info

from setuptools import setup, find_packages
from qingstor.sdk import __version__

ROOT = os.path.dirname(__file__)

with open('requirements.txt') as fp:
    requires = [item.strip() for item in fp.readlines()]

if version_info[:3] < (2, 7, 9):
    for item in requires:
        if item.startswith('requests'):
            requires.remove(item)
            requires.append('requests[security]')

if version_info[:3] < (2, 7, 0):
    requires.insert(0, 'idna<2.6,>=2.5')

setup(
    name='qingstor-sdk',
    version=__version__,
    description='The official QingStor SDK for the Python programming language.',
    long_description=open('README.md').read(),
    author='Yunify SDK Group',
    url='https://github.com/yunify/qingstor-sdk-python',
    author_email='sdk_group@yunify.com',
    scripts=[],
    packages=find_packages('.', exclude=["*.tests", "*.tests.*", "tests.*", "tests"]),
    namespace_packages=['qingstor'],
    package_dir={'sdk': 'qingstor'},
    include_package_data=True,
    install_requires=requires,
    license="Apache License 2.0",
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ], )
