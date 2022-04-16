
from sys import stdin

n = int(stdin.readline())
times = list(map(int, stdin.readline().split()))

times.sort()

total = 0
for i in range(n):
    total += (i + 1) * times[i]

print(total)
