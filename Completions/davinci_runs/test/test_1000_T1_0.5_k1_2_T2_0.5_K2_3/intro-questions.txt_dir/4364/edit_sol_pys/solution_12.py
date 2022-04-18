

import re

# Get inputs
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

# Get result
result = []
for i in range(N):
    result.append(str(sum(A[i:] + B[:(N - i)])))

# Output
print(" ".join(result))
