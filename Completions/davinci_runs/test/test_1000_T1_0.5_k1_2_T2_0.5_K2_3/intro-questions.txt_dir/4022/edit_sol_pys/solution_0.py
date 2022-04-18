

n = int(input())

x = []

for i in range(n):
    a, b = map(int, input().split())
    x.append((a, b))

x.sort()

ans = 0

for i in range(n):
    a = x[i][0]
    b = x[i][1]
    for j in range(i + 1, n):
        if a > x[j][0]:
            a = x[j][0]
        if b < x[j][1]:
            b = x[j][1]
        if a == b:
            break
    if b - a > ans:
        ans = b - a

print(ans)
