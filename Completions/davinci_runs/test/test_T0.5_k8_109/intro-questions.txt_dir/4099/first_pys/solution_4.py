

#input
N, K, M = map(int, input().split())
A = list(map(int, input().split()))

#output
if sum(A) / (N - 1) >= M:
    print(0)
elif K == M:
    print(-1)
else:
    print(M * N - sum(A))