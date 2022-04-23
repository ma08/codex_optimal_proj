# 파이썬은 이렇게 입력을 받는다.
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))


C = [0] * N
for i in range(N):
    C[i] = A[i] - B[i]


C.sort()

count = 0
for i in range(N):
    if C[i] > 0:
        count += C[i]

print(count)
