
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= M:
    print(0)
    exit()

if K + sumA >= M*N:
    print(M*N - sumA)
    exit()
else:
    print(-1)
