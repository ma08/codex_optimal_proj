n, m = map(int, input().split())
l = [input() for _ in range(m)]
ans = [-1] * n
for i in range(m):
    for j in range(n):
        if ans[j] == -1:
            ans[j] = l[i][j]
        else:
            if ans[j] != l[i][j]:
                print(-1)
                exit()
ans = int(''.join(map(str, ans)))
if ans > 10 ** 9:
    print(-1)
else:
    print(ans)
