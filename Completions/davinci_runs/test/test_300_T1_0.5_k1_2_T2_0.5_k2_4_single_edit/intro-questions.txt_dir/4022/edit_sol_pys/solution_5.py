
n, m = map(int, input().split())

x = []
y = []

for _ in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)

x = sorted(x)
y = sorted(y)

for i in range(n - 1):
    if x[i] == x[i + 1]:
        x[i] = 0
    if y[i] == y[i + 1]:
        y[i] = 0

x = list(set(x))
y = list(set(y))

if len(x) == 1:
    print(0)
else:
    print(max(y) - min(x))

