# ABC085C

N, Y = map(int, input().split())

for i in range(N + 1):
    for j in range(N + 1 - i):
        if 10000 * i + 5000 * j + 1000 * (N - i - j) == Y:
            print(i, j, N - i - j)
            exit()

for i in range(N):
    c, t = map(int, input().split())
    costs.append(c)
    times.append(t)

costs = [costs[i] for i in range(len(costs)) if times[i] <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
