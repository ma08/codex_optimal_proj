
N, T = map(int, input().split())
costs = []
times = []
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = list(sorted(costs))
times = list(sorted(times))

if times[0] > T:
    print("TLE")
else:
    print(costs[0])
