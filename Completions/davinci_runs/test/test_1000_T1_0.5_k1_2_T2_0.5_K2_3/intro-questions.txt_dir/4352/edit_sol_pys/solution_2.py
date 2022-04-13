

n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if a[j][i] + a[i][k] < a[j][k]:
                print(-1)
                exit()

ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i][j] > 0:
            ans += a[i][j]
print(ans)
