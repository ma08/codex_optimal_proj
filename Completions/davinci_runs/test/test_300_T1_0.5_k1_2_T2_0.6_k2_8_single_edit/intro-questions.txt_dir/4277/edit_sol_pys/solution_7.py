

import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))


A = sorted(A, reverse=True)


max_num = A[0]
min_num = A[len(A) - 1]

max_num_count = 0
min_num_count = 0

for i in range(N):
    if max_num == A[i]:
        max_num_count += 1

for j in range(N):
    if min_num == A[j]:
        min_num_count += 1

print(max_num - min_num, max_num_count * min_num_count)
