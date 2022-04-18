#!/usr/bin/env python3
n = int(input())
a = [input() for i in range(n)]
score = sum(1 for i in a if i == 'A')
print(score)
