

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

r = [0] * n
c = [0] * m

for i in range(n):
    if sum(a[i]) % 2 == 1:
        r[i] = 1

for j in range(m):
    if sum(a[i][j] for i in range(n)) % 2 == 1:
        c[j] = 1

if sum(r) % 2 == 1 and sum(c) % 2 == 1:
    print("NO")
else:
    print("YES")
    print("".join(map(str, r)))
    print("".join(map(str, c)))