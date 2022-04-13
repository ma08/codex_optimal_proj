
from bisect import bisect_left, bisect_right

N = int(input())
A = [int(input()) for i in range(N)]
B = [int(input()) for i in range(N)]
C = [int(input()) for i in range(N)]

A.sort()  # O(NlogN)

count = 0

for i in range(N):  # O(NlogN)
    count += bisect_left(A, B[i]) * (N - bisect_right(A, C[i]))

print(count)
