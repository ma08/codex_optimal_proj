#!/usr/bin/env python3

# Created by: Christina Ngwa
# Created on: October 2019
# This program calculates the sum of numbers in a list

import random


n = int(input())

a = list(map(int, input().split()))

s = a[0]

c = 1

for i in range(1, n):

    s += a[i]

    if s == 0:

        c += 1

        s = a[i]

print(c)
