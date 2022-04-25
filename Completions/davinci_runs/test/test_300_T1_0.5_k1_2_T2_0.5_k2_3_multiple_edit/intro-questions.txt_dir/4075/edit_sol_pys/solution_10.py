import sys
N, M = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
BC = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

A.sort(reverse=True)
BC.sort(key=lambda x: x[1], reverse=True)

cnt = 0
for b, c in BC:
    for i in range(b):
        if cnt >= N:
            break
        if A[cnt] < c:
            A[cnt] = c
        cnt += 1

print(sum(A))
