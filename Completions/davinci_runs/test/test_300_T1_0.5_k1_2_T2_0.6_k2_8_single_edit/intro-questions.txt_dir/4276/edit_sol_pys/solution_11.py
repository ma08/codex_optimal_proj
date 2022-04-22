# -*- coding: utf-8 -*-

N, T = map(int, input().split())

costs = []
times = []

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = [costs[i] for i in range(len(costs)) if times[i] <= T] # 費用リストのうち条件を満たすものを取り出す
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
