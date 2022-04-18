
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / float(N)

if avg >= M:
    print(0)
    exit()

if K <= M:
    print(-1)
    exit()

print(int(M*N - sumA))
