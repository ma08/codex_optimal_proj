
num = int(input()) # вводим число

while num >= 10: # пока наше число больше 9
    num = str(num) # переводим в строку
    num = [int(i) for i in num] # переводим в список
    num = [i for i in num if i != 0] # отсеиваем нули
    num = [str(i) for i in num] # переводим в строку
    num = ''.join(num) # объединяем список
    num = int(num) # переводим в число

print('Результат:', num)
