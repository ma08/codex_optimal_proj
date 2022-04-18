#!/usr/bin/env python3

n = int(input())
s = input()

print(max(s[i:i+2] for i in range(len(s) - 1)), key=s.count)
