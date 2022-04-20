
x = int(input())
b = 100.0
i = 0

while b < x:
    b += b * 0.01
    i += 1

print(i)
