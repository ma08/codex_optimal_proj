
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

ans = 0
for i in range(N):
    if A[i] != i + 1:
        continue
    if i % 2 == 0 and A[i] % 2 == 0:
        ans += 1
    if i % 2 == 1 and A[i] % 2 == 1:
        ans += 1

print(ans)
