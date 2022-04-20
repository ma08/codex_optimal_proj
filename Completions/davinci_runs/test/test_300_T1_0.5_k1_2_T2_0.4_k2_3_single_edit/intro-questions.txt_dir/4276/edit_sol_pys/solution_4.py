
N, T = map(int, input().split())

costs = []
times = []

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

valid_costs = [costs[i] for i in range(len(costs)) if times[i] <= T]
if len(valid_costs) == 0:
    print('TLE')
else:
    print(min(valid_costs))
