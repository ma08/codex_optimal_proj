
N, T = map(int, input().split())
costs = [0] * N
times = [0] * N
for i in range(N):
    c, t = map(int, input().split())
    costs[i] = c
    times[i] = t
costs = [costs[i] for i in range(N) if times[i] <= T]
if not costs:
    print('TLE')
else:
    print(min(costs))
