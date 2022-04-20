

N = int(input())
towns = [tuple(map(int, input().split())) for _ in range(N)]

import itertools

total = 0

for path in itertools.permutations(towns):
    total += sum(((path[i][0] - path[i+1][0]) ** 2 + (path[i][1] - path[i+1][1]) ** 2) ** 0.5 for i in range(N-1))

print(total / N)