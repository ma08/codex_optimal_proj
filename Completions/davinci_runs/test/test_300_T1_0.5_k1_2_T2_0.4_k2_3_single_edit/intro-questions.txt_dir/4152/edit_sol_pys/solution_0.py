#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (c) 2016 Felipe Gallego. All rights reserved.
#
# This is free software: you can redistribute it and/or modify it
# under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Script to solve the problem.
"""

import sys

def read_int():
    """Read an integer from standard input.
    """
    return int(sys.stdin.readline())

def read_list_int():
    """Read a list of integers from standard input.
    """
    return list(map(int, sys.stdin.readline().split()))

def solve(n, a):
    """Solve the problem.
    """
    s = set()
    for i in range(n):
        if a[i] not in s:
            s.add(a[i])
        else:
            s.remove(a[i])

    return n-len(s)

if __name__ == "__main__":
    
    n = read_int()
    
    a = read_list_int()
    
    print(solve(n, a))

