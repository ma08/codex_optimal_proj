

x = int(input("Введите количество денег: "))
b = 100
i = 0

while b < x:
    b += b // 100
    i += 1

print(i)
