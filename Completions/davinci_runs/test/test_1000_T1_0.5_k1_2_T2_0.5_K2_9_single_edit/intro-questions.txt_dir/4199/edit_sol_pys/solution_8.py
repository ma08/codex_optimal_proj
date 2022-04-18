import numpy as np

import sys

N, K = list(map(int, sys.stdin.readline().split()))
h = list(map(int, sys.stdin.readline().split()))

count = 0
for i in range(N):
    if h[i] >= K:
        count += 1


# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# count = 0
# for i in range(N):
#     count += B[A[i]-1]
#     if i >= 1:
#         if A[i-1]+1 == A[i]:
#             count += C[A[i-1]-1]

# print(count)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# A.sort(reverse=True)
# ans = 0
# for i in range(M):
#     if A[i] < 0:
#         break
#     ans += A[i]

# print(ans)

# N, M = map(int, input().split())
# A = list(map(int, input().split()))
# B = list(map(int, input().split()))
# C = list(map(int, input().split()))
# A.sort()
# B.sort()
# C.sort()
# ans = 0
# for b in B:
#     ans += bisect.bisect_left(A, b) * (N-bisect.bisect_right(C, b))

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# ans = 0
# for i in range(N):
#     while True:
#         if A[i] % 2 == 0:
#             A[i] /= 2
#             ans += 1
#         else:
#             break

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# ans = 0
# for i in range(N):
#     ans += B[A[i]-1]
#     if i >= 1 and A[i-1]+1 == A[i]:
#         ans += C[A[i-1]-1]

# print(ans)

# N, K = map(int, input().split())
# h = [int(i) for i in input().split()]

# dp = [float('inf')]*N
# dp[0] = 0
# for i in range(N):
#     for j in range(1, K+1):
#         if i+j < N:
#             dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))

# print(dp[N-1])

# N = int(input())
# A = [int(i) for i in input().split()]
# ans = 0
# for i in range(N):
#     while A[i] % 2 == 0:
#         A[i] /= 2
#         ans += 1

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# A.sort()
# B.sort()
# C.sort()

# ans = 0
# for b in B:
#     ans += bisect.bisect_left(A, b) * (N-bisect.bisect_right(C, b))

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# ans = 0
# for i in range(N):
#     while A[i] % 2 == 0:
#         A[i] /= 2
#         ans += 1

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# A.sort()
# B.sort()
# C.sort()

# ans = 0
# for b in B:
#     ans += bisect.bisect_left(A, b) * (N-bisect.bisect_right(C, b))

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# A.sort()
# B.sort()
# C.sort()

# ans = 0
# for b in B:
#     ans += bisect.bisect_left(A, b) * (N-bisect.bisect_right(C, b))

# print(ans)

# N = int(input())
# A = [int(i) for i in input().split()]
# B = [int(i) for i in input().split()]
# C = [int(i) for i in input().split()]

# A.sort()
# B.sort()
# C.sort()

# ans = 0
# for b in B:
#     ans += bisect.bisect_left(A, b) * (N-bisect.bisect_right(C, b))

# print(ans)

# N, K = map(int, input().split())
# h = [int(i) for i in input().split()]

# dp = [float('inf')]*N
# dp[0] = 0
# for i in range(N):
#     for j in range(1, K+1):
#         if i+j < N:
#             dp[i+j] = min(dp[i+j], dp[i]+abs(h[i]-h[i+j]))

# print(dp[N-1])
print(count)
