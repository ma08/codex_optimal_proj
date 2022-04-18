
N = int(input())
F = [[int(i) for i in input().split()] for _ in range(N)]
P = [int(i) for i in input().split()]

ans = -1000000000000
for i in range(1, 2**10):
    tmp = 0
    for j in range(N):
        cnt = 0
        for k in range(10):
            cnt += F[j][k] and (i >> k) & 1
        tmp += P[cnt]
    ans = max(ans, tmp)
print(ans)
