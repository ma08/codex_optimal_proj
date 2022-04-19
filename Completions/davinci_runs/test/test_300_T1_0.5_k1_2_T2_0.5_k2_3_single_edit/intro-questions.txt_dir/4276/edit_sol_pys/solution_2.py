
# coding: utf-8

N, T = map(int, input().split())  # 標準入力

costs = []
times = []

for i in range(N):
    c, t = map(int, input().split())  # 標準入力
    costs.append(c)
    times.append(t)

costs = [costs[i] for i in range(len(costs)) if times[i] <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
