
N, T = map(int, input().split())
costs = [int(input().split()[0]) for _ in range(N) if int(input().split()[1]) <= T]
if not costs:
    print('TLE')
else:
    print(min(costs))
