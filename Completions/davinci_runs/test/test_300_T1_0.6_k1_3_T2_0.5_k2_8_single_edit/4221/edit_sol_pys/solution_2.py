#!/usr/bin/env python3

s = input()
if s[-1:] == "s":
    print(s + "es", end='')
else:
    print(s + "s", end='')
