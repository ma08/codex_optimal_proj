
# coding: utf-8
N, T = map(int, input().split())

costs = []
times = []
# N個の料理、T秒以内にできる料理を抽出する
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)
# T秒以内にできる料理があるかどうか、あれば最安値を出力する

costs = [costs[i] for i in range(len(costs)) if times[i] <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
