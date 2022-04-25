

N, K = map(int, input().split())

A = []
for i in range(K):
    A.append(list(map(int, input().split()))[1:])

A_flat = []
for i in range(K):
    A_flat.extend(A[i])
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
