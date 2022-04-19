N, K, M = map(int, input().split())
A = [int(i) for i in input().split()]

sum_A = sum(A)
avg = sum_A / N

if avg >= M:
    print(0)
    exit()

if K <= M:
    print(-1)
    exit()

print(M*N - sum_A)
