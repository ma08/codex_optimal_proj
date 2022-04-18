

N, M = map(int, input().split())

l = []
for i in range(N):
    l.append(list(map(int, input().split())))

ans = 0
for i in range(N):
    for j in range(M):
        if l[i][j] == 1:
            continue
        if i == 0:
            if j == 0:
                ans = max(ans, l[i][j+1] + l[i+1][j])
            elif j == M-1:
                ans = max(ans, l[i][j-1] + l[i+1][j])
            else:
                ans = max(ans, l[i][j-1] + l[i+1][j] + l[i][j+1])
        elif i == N-1:
            if j == 0:
                ans = max(ans, l[i][j+1] + l[i-1][j])
            elif j == M-1:
                ans = max(ans, l[i][j-1] + l[i-1][j])
            else:
                ans = max(ans, l[i][j-1] + l[i-1][j] + l[i][j+1])
        else:
            if j == 0:
                ans = max(ans, l[i][j+1] + l[i-1][j] + l[i+1][j])
            elif j == M-1:
                ans = max(ans, l[i][j-1] + l[i-1][j] + l[i+1][j])
            else:
                ans = max(ans, l[i][j-1] + l[i-1][j] + l[i+1][j] + l[i][j+1])

print(ans)
