
N, T = map(int, input().split())

costs = []
times = []

for _ in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = [c for c, t in zip(costs, times) if t <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
