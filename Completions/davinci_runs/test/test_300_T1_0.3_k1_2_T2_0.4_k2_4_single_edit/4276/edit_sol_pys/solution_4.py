
N, T = map(int, input().split())
costs = []
times = []
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = sorted(costs, reverse=True)
times = sorted(times, reverse=True)

if times[0] > T:
    print("TLE")
else:
    print(costs[0])
