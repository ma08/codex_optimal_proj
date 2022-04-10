
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

for i in range(m):
    for j in range(n):
        print(a[j][i], end=" ")
    print()
