# -*- coding: utf-8 -*-

N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = input()

p = 0
for i in range(N):
    if i < K:
        if T[i] == 'r':
            p += P
        elif T[i] == 's':
            p += R
        else:
            p += S
    else:
        if T[i-K] == T[i]:
            T[i] = 'x'
        if T[i] == 'r':
            p += P
        elif T[i] == 's':
            p += R
        else:
            p += S
print(p)
