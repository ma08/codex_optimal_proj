

N, M, C = map(int, input().split())
B = list(map(int, input().split()))
A = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for a in A:
    res = 0
    for i in range(M):
        res += a[i] * B[i]
    res += C
    if res > 0:
        ans += 1
print(ans)
