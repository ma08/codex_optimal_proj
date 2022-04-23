#!/usr/bin/env python
# -*- coding: utf-8 -*-

n = int(input())
a = list(map(int, input().split()))

a.sort()

print(min(a[-1] - a[1], a[-2] - a[0]))
