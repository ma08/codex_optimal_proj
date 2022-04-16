
n, m = [int(x) for x in input().split()]
x = [int(x) for x in input().split()]
x.sort()

if m == 1:
    print(x[-1] - x[0])
    print(int((x[-1] + x[0]) / 2))
    exit(0)
if m == 2:
    print(x[-1] - x[0] + x[-2] - x[1])
    print(x[0], x[-1])
    exit(0)

res = 0
y = []
for i in range(1, m - 1):
    y.append(x[i])
    res += x[i] - x[i - 1]
y = [x[0]] + y + [x[-1]]
print(res + x[-1] - x[0])
print(*y)
