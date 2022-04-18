
import sys

b, d, c, length = map(int, sys.stdin.readline().split())  # вводим данные

if length % 2 != 0:
    print('impossible')  # проверка на нечетность
    sys.exit()

answers = []  # список ответов

for birds in range(length // b + 1):
    for dogs in range(length // d + 1):  # пробегаемся по всем вариантам
        for cats in range(length // c + 1):  # и добавляем в список
            if birds * b + dogs * d + cats * c == length:
                answers.append([birds, dogs, cats])

if len(answers) == 0:
    print('impossible')  # если нет ответов
else:
    for answer in sorted(answers):
        print(*answer)
