
import sys
N, K = map(int, sys.stdin.readline().rstrip().split())

prices = sorted(list(map(int, sys.stdin.readline().rstrip().split())))

total = 0
for i in range(K):
    total += prices[i]

print(total)
