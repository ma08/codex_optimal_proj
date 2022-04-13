
import sys

N = int(input())
A = list(map(int, input().split()))

for i in range(N):
    A[i] -= i+1

A.sort()

if N % 2 == 1:
    b = A[N//2]
else:
    b = (A[N//2-1] + A[N//2]) / 2

ans = 0
for i in range(N):
    ans += abs(A[i] - b)

print(ans)
