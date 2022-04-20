N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= M:
    print(0)
    exit(0)

if K <= M:
    print(-1)
    exit(0)

print(M*N - sumA)
