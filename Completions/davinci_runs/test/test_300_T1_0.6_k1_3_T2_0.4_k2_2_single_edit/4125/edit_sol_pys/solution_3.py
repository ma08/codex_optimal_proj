
import sys

N, X = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

A.sort()

# print(A)

m_diff = A[1] - A[0]

for i in range(1, len(A) - 1):
    m_diff = max(m_diff, A[i + 1] - A[i])

print(m_diff)
