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
def read_airways():
    """Reads all airways from ATS.txt

    Args:
        lines (tuple(string)): A tuple containing all the lines (file.read())

    Returns:
        (dict)
    """
    pass

def read_airway_info(line):
    """Reads airway heading data

    Args:
        line (string): Airway header line

    Returns:
        (string)    ident
    """
    if not line.startswith('A'):
        raise ValueError('Line does not start with A \'%s\'' % line)

    fragments = line.strip().split(',')

    if fragments[1] == '':
        raise ValueError('Could not read line \'%s\'' % line)

    return fragments[1]

def read_airway_waypoint(line):
    """

    Args:
        line (string): Airway waypoint line

    Returns:
        (dict)  ident, location [lon, lat]
    """
    if not line.startswith('S'):
        raise ValueError('Line does not start with S \'%s\'' % line)

    fragments = line.strip().split(',')

    try:
        return {
            'ident': fragments[1],
            'location': [float(fragments[3]), float(fragments[2])]
        }
    except Exception as error:
        raise ValueError('Could not read line \'%s\'' % line) from error

def read_waypoints(lines):
    """Reads all waypoints from Waypoints.txt

    Args:
        lines (tuple(string)): A tuple containing all the lines (file.read())

    Returns:
        (dict)
    """

    # change routine to iter()
    result = []

    for line in lines:
        # jump empty lines
        if line.strip() == "":
            continue

        try:
            result.append(read_waypoint(line))
        except Exception as error:
            # TODO: logging
            continue

    return result
    

def read_waypoint(line):
    """Reads and parses a single waypoint line from Waypoints.txt

    Args:
        line (string): A single line from Waypoints.txt file

    Returns:
        (dict)  ident, location [lon, lat], country
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
