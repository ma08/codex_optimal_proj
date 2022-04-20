#!/usr/bin/env python3
# -*- coding: utf-8 -*-


k = int(input())
s = input()

if len(s) <= k:
    print(s)
else:
    print(s[:k] + "...")
