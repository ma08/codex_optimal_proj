#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file.py
#  
#  Copyright 2019  <pi@raspberrypi>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  


import sys

n = int(sys.stdin.readline())

if n == 0:
    print(0)
    exit()

if n > 0:
    res = []
    while n > 0:
        res.append(str(n % 2))
        n //= 2
    print("".join(res[::-1]))
    exit()

# n < 0
n = abs(n)

res = []
while n > 0:
    if n % 2 == 0:
        res.append("1")
        n = (n // 2) + 1
    else:
        res.append("0")
        n //= 2

print("1" + "".join(res[::-1]))
