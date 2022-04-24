

x = int(input())
b = 1000
i = 0

while b < x:
    b += b // 100
    i += 1

print(i)
