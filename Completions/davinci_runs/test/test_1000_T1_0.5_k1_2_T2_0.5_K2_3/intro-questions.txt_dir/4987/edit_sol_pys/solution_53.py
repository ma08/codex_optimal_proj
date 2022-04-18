
from sys import stdin
from collections import deque

N, M = map(int, stdin.readline().split())
A = deque(map(int, stdin.readline().split()))

for i in range(M):
    B = deque(map(int, stdin.readline().split()))

    while len(B) > 0:
        if B[0] == A[0]:
            A.popleft()
            B.popleft()
        elif B[0] == A[-1]:
            A.pop()
            B.popleft()
        else:
            break

if len(A) == 0:
    print('YES')
else:
    print('NO')
