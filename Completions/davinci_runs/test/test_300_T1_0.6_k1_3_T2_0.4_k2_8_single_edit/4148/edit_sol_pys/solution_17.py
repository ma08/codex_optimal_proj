#!/usr/bin/env python3

n = int(input())
s = input().strip()

for i in range(len(s)):
    s = s[:i] + chr(ord(s[i]) + n % 26) + s[i + 1:]

print(s)
