#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

n = int(sys.stdin.readline()) % 26
s = sys.stdin.readline()

for i in range(len(s)):
    if ord(s[i]) + n > ord('Z'):
        print(chr(ord(s[i]) + n - 26), end='')
    else:
        print(chr(ord(s[i]) + n), end="")
