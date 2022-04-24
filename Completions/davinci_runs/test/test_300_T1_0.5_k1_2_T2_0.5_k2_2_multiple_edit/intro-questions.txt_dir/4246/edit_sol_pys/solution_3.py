# -*- coding: utf-8 -*-

s = input() # string
t = input() # string

correct = 0

for i in range(len(s)):
    if s[i] == t[i]:
        correct += 1

print(correct)
