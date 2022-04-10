
# SOLUTION

n, m = map(int, input().split())

a = []
b = []
for i in range(m):
    tmp = list(map(int, input().split()))
    a.append(tmp[1:])
    b.append(tmp[0])

p = list(map(int, input().split()))

result = 0
for bits in range(2 ** n):
    ok = True
    for i in range(m):
        cnt = 0
        for j in range(b[i]):
            if bits & (1 << (a[i][j] - 1)):
                cnt += 1
        if cnt % 2 != p[i]:
            ok = False
    if ok:
        result += 1

print(result)
