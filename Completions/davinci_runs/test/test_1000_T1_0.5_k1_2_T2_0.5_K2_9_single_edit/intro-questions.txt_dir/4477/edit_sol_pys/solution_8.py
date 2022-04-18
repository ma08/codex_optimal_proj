#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file.py
#  
#  Copyright 2018 yorlysoro <yorlysoro@gmail.com>
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

def solve(x):
    ans = 0
    for i in range(1, x // 10 + 1):
        ans += i * (9 - x//(10**i)%10)
    return ans

def main():
    t = int(input())
    for i in range(t):
        x = int(input())
        print(solve(x))

if __name__ == "__main__":
    main()
