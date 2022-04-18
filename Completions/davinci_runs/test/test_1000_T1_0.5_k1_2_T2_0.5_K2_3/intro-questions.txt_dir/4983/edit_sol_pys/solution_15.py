
num = int(input())  # вводим число

while num > 9:  # пока число больше 9
    num = str(num)  # переводим в строку
    num = [int(i) for i in num]  # переводим в список
    num = [i for i in num if i != 0]  # удаляем нули
    num = [str(i) for i in num]  # переводим в строку
    num = ''.join(num)  # объединяем в строку
    num = int(num)  # переводим в число

print(num)
