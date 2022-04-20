import sys

N, K = map(int, sys.stdin.readline().split())
H = list(map(int, sys.stdin.readline().split()))

result = 0

for i in H:
    if i >= K:
        result += 1
print(result)
