#!/usr/bin/env python
"""
Route Planner API.
Copyright (C) 2017  Pedro Rodrigues <prodrigues1990@gmail.com>

Route Planner API is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

Route Planner API is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Route Planner API.  If not, see <http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

setup(
    name='Route Planner API',
    version='0.1',
    description = 'Route Planner API',
    author = 'Pedro Rodrigues',
    author_email = 'prodrigues1990@gmail.com',
    packages = find_packages(),
    install_requires = [],
    test_suite = 'tests'
)
