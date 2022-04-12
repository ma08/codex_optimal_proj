#!/usr/bin/env python3
s = input()
t = input()

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
