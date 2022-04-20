

import sys
import math

# read input
N = int(input())
A = [int(a) for a in input().split()]
B = [int(b) for b in input().split()]
C = [int(c) for c in input().split()]

# solve
ans = 0
for i in range(N-1):
    ans += B[A[i]-1]
    if A[i+1] == A[i]+1:
        ans += C[A[i]-1]
ans += B[A[N-1]-1]

# output
print(ans)