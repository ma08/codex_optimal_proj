#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file.py
#  
#  Copyright 2020 contributors of cardgame
#  
#  This file is part of cardgame.
#
#  cardgame is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  cardgame is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with cardgame.  If not, see <http://www.gnu.org/licenses/>.
#


def solve(n, sequence):
    if n == 1:
        return 0
    elif n == 2:
        return 0
    else:
        diff = sequence[1] - sequence[0]
        i = 2
        while i < n:
            if sequence[i] - sequence[i-1] != diff:
                return -1
            i += 1
        return 0


if __name__ == '__main__':
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(solve(n, sequence))
