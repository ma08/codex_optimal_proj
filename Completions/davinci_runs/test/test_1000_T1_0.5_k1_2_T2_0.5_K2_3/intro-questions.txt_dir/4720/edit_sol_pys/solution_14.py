
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort(reverse=True)
if N >= M:
    print(0)
else:
    print(sum(A[N:]))
