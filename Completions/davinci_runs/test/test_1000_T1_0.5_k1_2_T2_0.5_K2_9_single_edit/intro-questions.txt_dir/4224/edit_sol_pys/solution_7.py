
import sys

# input
N = int(input())
A = list(map(int, input().split()))

# solve
ans = 0
for i in range(N):
    while A[i] % 2 == 0 or A[i] % 3 == 2:
        A[i] -= 1
        ans += 1

print(ans)
