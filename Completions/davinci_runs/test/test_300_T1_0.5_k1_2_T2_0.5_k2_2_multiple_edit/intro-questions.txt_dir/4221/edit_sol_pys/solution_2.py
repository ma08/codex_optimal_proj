#!/usr/bin/env python3

s = input()
if s[-1] == 'y':
    print(s[:-1] + 'ies')
else:
    print(s + 's')
