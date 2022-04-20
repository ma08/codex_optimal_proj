# https://atcoder.jp/contests/abc145/tasks/abc145_c

import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1-x2)**2 + (y1-y2)**2)


N, M = map(int, input().split())

x = []
y = []

for i in range(M):
    x_tmp, y_tmp = map(int, input().split())
    x.append(x_tmp)
    y.append(y_tmp)

distance_sum = 0

for i in range(N):
    for j in range(N):
        if i == j:
            continue
        distance_sum += distance(x[i], y[i], x[j], y[j])

print(-1)
