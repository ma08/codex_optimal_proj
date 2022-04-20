
N = int(input())
A = list(map(int, input().split()))
d = {}
for i in range(N):
    if A[i] in d:
        d[A[i]] += 1
    else:
        d[A[i]] = 1
for i in range(1, N+1):
    if i in d:
        print(d[i])
    else:
        print(0)
