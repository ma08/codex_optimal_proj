#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  file
#  
#  Copyright 2018 youcef sourani <youssef.m.sourani@gmail.com>
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

n = int(input())
s = input()

#s = '120110'
#n = len(s)

a = [0,0,0]
for i in range(n):
    a[int(s[i])] += 1

#print(a)

if a[1] == a[2]:
    print(s)
else:
    k = a[1] - a[2]
    if k < 0:
        k = -k
    r = k // 3
    if k % 3 != 0:
        r += 1
    #print(r)
    a[1] -= r
    a[2] += r
    #print(a)
    ans = ''
    for i in range(n):
        if a[0] > 0:
            ans += '0'
            a[0] -= 1
        elif a[1] > 0:
            ans += '1'
            a[1] -= 1
        elif a[2] > 0:
            ans += '2'
            a[2] -= 1
    print(ans)
