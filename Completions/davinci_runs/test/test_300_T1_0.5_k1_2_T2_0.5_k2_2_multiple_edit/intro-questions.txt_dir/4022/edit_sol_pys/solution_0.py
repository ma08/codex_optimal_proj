

# Solution

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


# Solution

n = int(input())

y = []
x = []

for i in range(n):
    a, b = map(int, input().split())
    x.append((a, b, i))
    y.append(x[i][0])

y.sort()

ans = 0

for i in range(n):
    a = x[i][1]
    b = y[i]
    if a - b > ans:
        ans = a - b

print(ans)
