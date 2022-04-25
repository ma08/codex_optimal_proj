
N, K = map(int, input().split())

A = []
for i in range(K):
    d = int(input())
    A.append(list(map(int, input().split())))

A_set = set()
for i in A:
    A_set.update(i)

ans = N - len(A_flat)
print(ans)
