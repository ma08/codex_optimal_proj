

n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]

rows = [0]*n
cols = [0]*m
for i in range(n):
    for j in range(m):
        if a[i][j] == 1:
            rows[i] += 1
            cols[j] += 1

if max(rows) > n//2 or max(cols) > m//2:
    print("NO")
else:
    print("YES")
    for i in range(n):
        if rows[i] > n//2:
            print("1", end="")
        else:
            print("0", end="")
    print()
    for j in range(m):
        if cols[j] > m//2:
            print("1", end="")
        else:
            print("0", end="")
    print()