

# Solution 1

n = int(input())

x = []
y = []

for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)

x.sort()
y.sort()

a = 0
b = 0

for i in range(n - 1):
    if x[i] == x[i + 1]:
        a += 1
    if y[i] == y[i + 1]:
        b += 1

if a == n - 1 or b == n - 1:
    print(0)
else:
    print(y[b] - x[a])


# Solution 2

n = int(input())

x = []

for i in range(n):
    a, b = map(int, input().split())
    x.append((a, b, i))

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