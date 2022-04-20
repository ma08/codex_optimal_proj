
n = int(input())
d = [int(x) for x in input().split()]

x = 1
y = 1

for i in range(1, n):
    if d[i] % x == 0:
        y *= d[i]
    else:
        x *= d[i]

print(x, y)
