
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= M and K <= M:
    print(0)
    exit()

print(M*N - sumA)
