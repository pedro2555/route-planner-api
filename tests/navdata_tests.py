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
    @file_data('test_read_airways.json')
    def test_read_airways(self, lines, airways):
        """Assert correct number of waypoints per airway"""
        test = navdata.read_airways(lines)

        # test for same number of airways
        self.assertEqual(len(test), len(airways))

        for test_airway, airway in zip(test, airways):
            # test airway identification
            self.assertEqual(test_airway['airway'], airway['airway'])

            # test for same number of waypoints
            self.assertEqual(len(test_airway['waypoints']), len(airway['waypoints']))

            # validate waypoint names
            for test_waypoint, waypoint in zip(test_airway['waypoints'], airway['waypoints']):
                self.assertEqual(test_waypoint['ident'], waypoint['ident'])

    @unpack
    @file_data('test_read_airway_waypoints.json')
    def test_read_airway_waypoints(self, lines):
        """Assert correct number of waypoints in result"""
        test = navdata.read_airway_waypoints(lines)

        # remove empty lines from test
        lines = list(filter(lambda line: line != '', lines))
        self.assertEqual(len(test), len(lines))

    @unpack
    @file_data('test_read_airway_waypoint.json')
    def test_read_airway_waypoint(self, line, ident, location):
        """Assert dict assignment"""
        test = navdata.read_airway_waypoint(line)

        self.assertIsNotNone(test)
        self.assertEqual(test['ident'], ident)
        self.assertEqual(test['location'], location)

    @data('F,LOTEE,44.658750,-5.836639,MEGAT,43.498861,-7.596472,233,230,102.94')
    def test_read_airway_waypoint_error(self, line):
        """Raises usefull exception info"""
        self.assertRaisesRegex(
            ValueError,
            '^.*%s.*$' % line,
            navdata.read_airway_waypoint,
            line)

    @unpack
    @file_data('test_read_airway_info.json')
    def test_read_airway_info(self, line, ident):
        """Assert dict assignment"""
        test = navdata.read_airway_info(line)

        self.assertIsNotNone(test)
        self.assertEqual(test, ident)

    @data('A,,7', 'F,A5,24')
    def test_read_airway_info_error(self, line):
        """Raises usefull exception info"""
        self.assertRaisesRegex(
            ValueError,
            '^.*%s.*$' % line,
            navdata.read_airway_info,
            line)

    @unpack
    @file_data('test_read_waypoints.json')
    def test_read_waypoints(self, lines, waypoint_count):
        """"""
        test = navdata.read_waypoints(lines)

        self.assertEqual(len(test), waypoint_count)

    @unpack
    @file_data('test_read_waypoint.json')
    def test_read_waypoint(self, line, ident, location, country):
        """Assigns waypoint data correctly"""
        test = navdata.read_waypoint(line)

        self.assertIsNotNone(test)
        self.assertEqual(test['ident'], ident)
        self.assertEqual(test['location'], location)
        self.assertEqual(test['country'], country)

    @data('0000E,0.000a00,0.000000,  ')
    def test_read_waypoint_error(self, line):
        """Raises usefull exception info"""
        self.assertRaisesRegex(
            ValueError,
            '^Could not read line \'%s\'$' % line,
            navdata.read_waypoint,
            line)
