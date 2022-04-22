
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A)
avg = sumA / N

if avg >= K:
    print(0)
    exit()

if M <= avg:
    print(-1)
    exit()

print(M*N - sumA)
