

x = int(input())
b = 100
i = 0

while b < x:
    b += b // 10
    i += 1

print(i)
