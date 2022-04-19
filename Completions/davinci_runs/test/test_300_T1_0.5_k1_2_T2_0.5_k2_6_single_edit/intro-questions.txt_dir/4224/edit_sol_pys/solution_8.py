
import sys


# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1

print(ans)
