
N, T = map(int, input().split())
costs = []
times = []
for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs_sorted = sorted(costs)
times_sorted = sorted(times)

if times_sorted[0] > T:
    print("TLE")
else:
    print(costs_sorted[0])
