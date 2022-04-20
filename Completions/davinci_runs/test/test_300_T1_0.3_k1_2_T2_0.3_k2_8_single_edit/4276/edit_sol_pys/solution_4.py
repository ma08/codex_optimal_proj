
N, T = map(int, input().split())
costs = []
times = []
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = sorted(costs, key=lambda x: x[0])
times = sorted(times, key=lambda x: x[1])

if times[0] > T:
    print("TLE")
else:
    print(costs[0])
