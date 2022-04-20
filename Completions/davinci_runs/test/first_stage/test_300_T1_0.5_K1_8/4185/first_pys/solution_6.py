

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

# print(a)

res = 0
for i in range(n):
    for j in range(m):
        if a[i][j] != (i * m + j + 1):
            for k in range(j + 1, m):
                if a[i][k] == (i * m + j + 1):
                    for x in range(k, j, -1):
                        a[i][x], a[i][x - 1] = a[i][x - 1], a[i][x]
                        res += 1
                    break
            else:
                print(-1)
                exit()

print(res)