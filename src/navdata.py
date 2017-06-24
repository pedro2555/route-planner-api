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
def read_waypoint(line):
    """Reads and parses a single waypoint line from Waypoints.txt

    Args:
        line (string): A single line from Waypoints.txt file

    Returns:
        (Dict)  ident, location [lon, lat], country
    """
    fragments = line.strip().split(',')

    try:
        return {
            'ident': fragments[0].strip(),
            'location': [float(fragments[2]), float(fragments[1])],
            'country': fragments[3] if len(fragments) > 3 else ''
        }
    except Exception as error:
        raise ValueError('Could not read line \'%s\'' % line) from error
