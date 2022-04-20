

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(str, input())))

cnt = 0
for i in range(n):
    for j in range(m):
        if a[i][j] == '*':
            cnt = cnt + 1

if cnt == 0:
    print(0)
else:
    print(cnt)
    for i in range(n):
        for j in range(m):
            if a[i][j] == '*':
                k = 1
                while i+k < n and j+k < m and i-k >= 0 and j-k >= 0:
                    if a[i+k][j] == '*' and a[i-k][j] == '*' and a[i][j+k] == '*' and a[i][j-k] == '*':
                        k = k + 1
                    else:
                        break
                print(i+1, j+1, k)
                for l in range(k):
                    a[i+l][j] = '.'
                    a[i-l][j] = '.'
                    a[i][j+l] = '.'
                    a[i][j-l] = '.'