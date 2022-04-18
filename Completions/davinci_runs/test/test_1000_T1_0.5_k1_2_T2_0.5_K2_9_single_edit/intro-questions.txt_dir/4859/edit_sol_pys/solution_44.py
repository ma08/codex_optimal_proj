
import sys

b, d, c, l = map(int, sys.stdin.readline().split()) # на вход принимаем 4 числа

if l % 2 != 0: # если последнее число нечетное, то выводим impossible
    print('impossible')
    sys.exit() # и завершаем программу

answers = [] # создаем пустой список для ответов

for birds in range(l // b + 1): # пробегаемся по всем возможным комбинациям чисел
    for dogs in range(l // d + 1):
        for cats in range(l // c + 1):
            if birds * b + dogs * d + cats * c == l: # если последнее число равно сумме всех предыдущих, то добавляем этот ответ в список
                answers.append([birds, dogs, cats])

if len(answers) == 0: # если ответов нет, то выводим impossible
    print('impossible')
else:
    for answer in sorted(answers): # иначе выводим все ответы по порядку
        print(*answer)
