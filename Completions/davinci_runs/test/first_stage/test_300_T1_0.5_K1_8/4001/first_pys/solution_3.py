

n = int(input())
d = [int(x) for x in input().split()]

x = 1
y = 1

for i in range(n):
    x *= d[i]
    if i % 2 == 1:
        y *= d[i]

print(x, y)