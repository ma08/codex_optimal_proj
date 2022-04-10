

n = int(input())
d = list(map(int, input().split()))

x = 1
y = 1

for i in d:
    if i % x == 0:
        y *= i
    else:
        x *= i

print(x, y)