# -*- coding: utf-8 -*-
import itertools

a, b, x = map(int, input().split())

s = ['0'] * a + ['1'] * b
ans = []

for t in itertools.permutations(s):
    cnt = 0
    for i in range(a + b):
        if i < a + b - 1 and t[i] == '0' and t[i+1] == '1':
            cnt += 1
    if cnt == x:
        ans.append(''.join(t))

print(sorted(ans)[0])
