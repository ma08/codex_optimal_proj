

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if sum(A) / (N - 1) >= M:
    print(0)
elif (sum(A) + K) / N < M:
    print(-1)
else:
    print(int(M * N - sum(A)))