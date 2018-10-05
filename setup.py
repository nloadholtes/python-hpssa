# Copyright 2015 Jared Rodriguez (jared at blacknode dot net)
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License");
#    you may not use this file except in compliance with the License.
#    You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS,
#    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#    See the License for the specific language governing permissions and
#    limitations under the License.

from setuptools import setup

setup(
    name='python-hpssa',
    version='0.0.12',
    packages=['hpssa'],
    url='',
    license='Apache-2.0',
    author='Jared Rodriguez',
    author_email='jared@blacknode.net',
    description='Python module for working with HP Smart Array controllers',
    install_requires=[
        'python-size'
    ]
)
