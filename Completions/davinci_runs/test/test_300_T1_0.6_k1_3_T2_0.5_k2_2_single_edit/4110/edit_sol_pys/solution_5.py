# input
N, M = map(int, input().split())
sc = [list(map(int, input().split())) for _ in range(M)]


# solve
ans = 'IMPOSSIBLE'
for i in range(1 << N):
    st = [0 for _ in range(N)]
    for j in range(N):
        if (i >> j) & 1:
            st[j] = 1

# initialize
ans = G
dp = [0 for _ in range(D)]

# solve
for i in range(D):
    dp[i] = pc[i][0] * 100 * (i+1) + pc[i][1]
    if dp[i] >= G:
        ans = min(ans, pc[i][0])
        break

if ans == G:
    for i in range(D-1, -1, -1):
        if dp[i] < G:
            for j in range(i, -1, -1):
                if pc[j][0] > 0:
                    cnt = (G - dp[i]) // (100 * (j+1))
                    if cnt >= pc[j][0]:
                        ans = min(ans, pc[j][0] + (i+1))
                        dp[i] += pc[j][0] * 100 * (j+1)
                        pc[j][0] = 0
                    else:
                        ans = min(ans, cnt + (i+1))
                        dp[i] += cnt * 100 * (j+1)
                        pc[j][0] -= cnt
            break

# output
print(ans)
