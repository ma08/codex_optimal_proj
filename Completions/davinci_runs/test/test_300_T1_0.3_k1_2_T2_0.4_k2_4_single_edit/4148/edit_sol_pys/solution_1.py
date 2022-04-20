# -*- coding: utf-8 -*-

import sys

n = int(input())
s = input().rstrip()

for i in range(len(s)):
    if ord(s[i]) + n > 90:
        print(chr(ord(s[i]) + n - 26), end="")
    else:
        print(chr(ord(s[i]) + n), end="")
