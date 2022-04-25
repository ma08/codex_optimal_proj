#!/usr/bin/python3

import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().split('\n')[0]
print(s)
for i in range(len(s)):
    if ord(s[i]) + n > ord('Z'):
        print(chr(ord(s[i]) + n - 26), end="")
    else:
        print(chr(ord(s[i]) + n), end="")
