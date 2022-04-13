x = int(input())

while x > 9:
    y = 1  # произведение цифр
    for i in str(x):
        if i != '0':  # чтобы не было произведение нулей
            y *= int(i)
    x = y

print(x)
