
n = int(input())
d = [int(x) for x in input().split()]

x = d[0]
y = 1

for i in range(n):
    if d[i] % x == 0:
        y *= d[i]
    else:
        x *= d[i]

print(x, y)
