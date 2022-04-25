#!/usr/bin/env python3

a, b, c = map(int, input().split())
if a+b+c >= 22:
    print('bust')
else:
    print('win')
