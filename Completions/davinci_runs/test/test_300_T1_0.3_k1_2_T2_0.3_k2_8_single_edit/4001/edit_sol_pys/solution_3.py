

n = int(input())
d = [int(x) for x in input().split()]

x = d[0] // 2
y = d[0] // 2

for i in range(1, n):
    if d[i] % x == 0 and d[i] // 2 > y:
        y = d[i] // 2
    else:
        x = d[i] // 2

print(x, y)
