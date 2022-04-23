
n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(m)]
ans = [0] * n
for i in range(m):
    for j in range(n):
        if ans[j] == 0:
            ans[j] = l[i][j] + 1
        else:
            if ans[j] != l[i][j] + 1:
                print(-1)
                exit()
ans = int(''.join(map(str, ans)))
if ans > 10 ** 9:
    print(-1)
else:
    print(ans)
