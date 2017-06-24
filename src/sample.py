#!/usr/bin/env python
"""
unittest boilerplate.
Copyright (C) 2017  Pedro Rodrigues <prodrigues1990@gmail.com>

unittest boilerplate is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, version 2 of the License.

unittest boilerplate is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with unittest boilerplate.  If not, see <http://www.gnu.org/licenses/>.
"""
def merge_sort(array):
    """Returns array sorted in ascending order

    Args:
        array (array): list of elements to sort
    """
    # base case, a single item array is also sorted
    if len(array) <= 1:
        return array

    # split the array in half
    lenght = len(array)
    array1 = array[0:int(lenght/2)]
    array2 = array[int(lenght/2):lenght]

    array1 = merge_sort(array1)
    array2 = merge_sort(array2)

    return merge(array1, array2)

def merge(array1, array2):
    """Merges two previously sorted arrays into a sorted array
    using two finger algorithm

    Args:
        array1 (array): A sorted array of n elements
        array2 (array): A sorted array of n elements
    """
    array3 = []
    # while both arrays have at least one value
    while array1 and array2:
        # append the smallest value into the result array and remove it from the origin
        if array1[0] > array2[0]:
            array3.append(array2[0])
            del array2[0]
        else:
            array3.append(array1[0])
            del array1[0]

    # if any of the arrays empties out just append the other one as is (it should be sorted anyway)
    while array1:
        array3.append(array1[0])
        del array1[0]

    while array2:
        array3.append(array2[0])
        del array2[0]

    return array3
