

import sys

# INPUT
N = int(input())
A = list(map(int, input().split()))

# SOLVE
ans = 0
for i in range(N):
    while A[i] % 2 == 0:
        A[i] /= 2
        ans += 1


# OUTPUT
print(ans)
print(ans)
