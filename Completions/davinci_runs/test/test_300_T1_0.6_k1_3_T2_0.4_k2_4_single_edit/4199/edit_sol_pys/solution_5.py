import sys
N, K = map(int, sys.stdin.readline().split())
h = list(map(int, sys.stdin.readline().split()))

result = 0

for i in h:
    if i >= K:
        result += 1
print(result)
