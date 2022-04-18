
N, K = map(int, input().split())

A = []
for i in range(K):
    _ = int(input())
    A.append(list(map(int, input().split())))

A_flat = []
for a in A:
    A_flat.extend(a)
A_flat = set(A_flat)

ans = N - len(A_flat)
print(ans)
