

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) / (N-1) >= M:
    print(-1)
else:
    print(M * N - sum(A))