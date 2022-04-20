

import numpy as np

def solution(n, k, s):
    d = {}
    for i in range(n):
        if s[i] in d:
            d[s[i]] += 1
        else:
            d[s[i]] = 1
    d = sorted(d.items(), key = lambda x: x[1], reverse = True)
    t = []
    for i in range(k):
        t.append(d[i][0])
    return t

n, k = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]

t = solution(n, k, s)
print(*t)