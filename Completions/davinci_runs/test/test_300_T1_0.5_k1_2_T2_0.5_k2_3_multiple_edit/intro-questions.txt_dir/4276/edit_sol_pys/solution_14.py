

N, K = list(map(int, input().split()))

costs = []
times = []

for i in range(N):
    c, t = list(map(int, input().split()))
    costs.append(c)
    times.append(t)

costs = [costs[i] for i in range(len(costs)) if times[i] <= K]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
