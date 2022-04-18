
N, T = map(int, input().split())

costs = {}

for i in range(N):
    c, t = map(int, input().split())
    costs[t] = c

costs = [costs[i] for i in costs.keys() if i <= T]
if len(costs) == 0: # 最小がない場合
    print('TLE')
else:
    print(min(costs))
