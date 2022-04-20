
N, T = map(int, input().split())
costs = [int(input().split()[0]) for i in range(N) if int(input().split()[1]) <= T]
if len(costs) == 0:
    print('TLE')
else:
    print(min(costs))
