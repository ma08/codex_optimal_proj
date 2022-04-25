
N, M = map(int, input().split())
A = list(map(int, input().split()))

A.sort()
A.reverse()

s = 0
c = 0
for i in range(M):
    if s >= N:
        break
    s += A[i]
    c += 1

print(c)
