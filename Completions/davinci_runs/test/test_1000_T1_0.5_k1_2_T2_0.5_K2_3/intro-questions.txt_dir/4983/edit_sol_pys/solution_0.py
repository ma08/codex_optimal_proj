

x = int(input("Введите число: "))
y = 0
while x > 0:
    y += x % 10
    x //= 10
print(y)
