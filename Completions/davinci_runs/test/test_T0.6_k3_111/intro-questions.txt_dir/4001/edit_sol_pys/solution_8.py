n = int(input())
a = [int(x) for x in input().split()]
a.sort()

x, y = 1, 1
for i in range(len(a)):
    if i % 2 == 0:
        x *= a[i]
    else:
        y *= a[i]

print(x, y)
