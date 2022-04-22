
N, T = map(int, input().split())

costs = []
times = []

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)
    if t <= T:
        costs.append(c)
        times.append(t)
if len(costs) == 0 or len(times) == 0:
    print('TLE')
else:
    print(min(costs))
