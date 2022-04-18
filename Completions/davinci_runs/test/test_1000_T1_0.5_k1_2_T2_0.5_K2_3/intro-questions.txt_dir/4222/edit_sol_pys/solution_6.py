

N, K = map(int, input().split(" "))

A = []
for i in range(K):
    d = int(input())
    A.append(list(map(int, input().split(" "))))

A_flat = set()
for i in range(K):
    A_flat.update(A[i])

ans = N - len(A_flat)
print(ans)
