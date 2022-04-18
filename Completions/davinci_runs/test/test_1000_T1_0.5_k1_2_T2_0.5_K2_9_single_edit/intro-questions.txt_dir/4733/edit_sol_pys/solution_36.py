

n, shuffle = input().split()  # вводим кол-во карт и направление стопки
n = int(n)  # кол-во карт

if shuffle == 'out':  # если стопка по возрастанию
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n // 2) + 1)
else:  # если стопка по убыванию
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2)
