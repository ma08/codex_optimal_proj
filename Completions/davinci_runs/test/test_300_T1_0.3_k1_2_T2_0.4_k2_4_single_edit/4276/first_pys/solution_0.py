

N, T = map(int, input().split())

costs = []
for _ in range(N):
    cost, time = map(int, input().split())
    if time <= T:
        costs.append(cost)

if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))