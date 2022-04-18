# -*- coding: utf-8 -*-

S = input()

count = 0
for s in S:
    if s == "+":
        count += 1
    elif s == "-":
        count -= 1
print(count)
