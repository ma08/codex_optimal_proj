n = int(input())
d = [int(x) for x in input().split()]
d.sort()

x = 1
y = 1
for i in range(len(d)):
    if i % 2 == 0:
        x *= d[i]
    else:
        y *= d[i]
print(x, y)
