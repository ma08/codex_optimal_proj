
N, K = map(int, input().split())

A = [set(map(int, input().split())) for _ in range(K)]

A_flat = []
for i in range(K):
    A_flat.extend(A[i])
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
