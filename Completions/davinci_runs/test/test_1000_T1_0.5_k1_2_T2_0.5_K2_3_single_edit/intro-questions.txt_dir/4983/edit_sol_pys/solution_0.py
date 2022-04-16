
x = int(input())
y = 1
while x > 9:
    z = x % 10
    if z > 0:
        y *= z
    x //= 10
print(y * x)
