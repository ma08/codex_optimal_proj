N, K, M = map(int, input().split())
A = list(map(int, input().split()))

sum_a = sum(A)
avg = sum_a / N

if avg >= M:
    print(0)
    exit()

if K <= M:
    print(-1)
    exit()

print(M * N - sum_a)
