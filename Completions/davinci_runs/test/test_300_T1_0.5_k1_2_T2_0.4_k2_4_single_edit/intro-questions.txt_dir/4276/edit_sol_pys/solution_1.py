
N, T = map(int, input().split())

costs = []
times = []

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = [costs[i] for i in range(N) if times[i] <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
