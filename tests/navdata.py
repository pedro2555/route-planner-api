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
import unittest
from ddt import ddt, unpack, file_data, data

from src import navdata

@ddt
class NavdataTests(unittest.TestCase):
    """Test suite for navdata module

    AIRAC data Aerosoft Airbus by Navigraph"""

    @unpack
    @file_data('waypoints_tests.json')
    def test_read_waypoint(self, line, ident, location, country):
        """Test reading a single waypoint line from Waypoints.txt"""
        test = navdata.read_waypoint(line)
        
        self.assertIsNotNone(test)
        self.assertEqual(test['ident'], ident)
        self.assertEqual(test['location'], location)
        self.assertEqual(test['country'], country)
