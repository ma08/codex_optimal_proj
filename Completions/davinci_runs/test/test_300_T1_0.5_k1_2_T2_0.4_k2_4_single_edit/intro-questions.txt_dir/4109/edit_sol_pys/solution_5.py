

N, M = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

for i in range(N):
    for j in range(M):
        if a[i] == b[j]:
            ans = min(ans, a[i])

# すべてのアルゴリズムのレベルがX以上になれば、コストが最小値になる
if ans == 10**10:
    print(-1)
else:
    print(ans)
