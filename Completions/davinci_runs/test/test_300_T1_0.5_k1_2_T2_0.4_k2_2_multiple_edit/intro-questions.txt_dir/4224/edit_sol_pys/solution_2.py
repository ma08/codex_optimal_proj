
import sys, math

# input
N, K = map(int, input().split())
A = list(map(int, input().split()))[:N]

# solve
ans = math.ceil(math.log2(max(A)))
if K >= ans:
    print('Yes')
else:
    print('No')
