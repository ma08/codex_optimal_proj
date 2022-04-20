

N, K, M = map(int, input().split())
A = list(map(int, input().split()))

if N == 1:
    print(0)
    exit()

S = sum(A) + M * N

for i in range(1, N):
    if S / i < K:
        print(i)
        exit()

print(-1)
