

import sys
import math

s = sys.stdin.readline()
s = s.rstrip()
s = s.split()

#s = "10 ghost mummy witch demon demon demon demon demon demon demon"  # ввод строки
#s = s.split()

n = int(s[0])  # количество слов в строке
s = s[1:]

d = {}  # словарь

for i in range(n):  # пробегаемся по словам из строки
    if s[i] not in d:
        d[s[i]] = 1  # если слово еще не встречалось, то добавляем в словарь и присваиваем 1
    else:
        d[s[i]] += 1  # если слово уже есть в словаре, то прибавляем 1

m = max(d.values())  # находим максимальное значение

for k, v in d.items():  # пробегаемся по словарю
    if v == m:
        print(k)  # если значение равно максимальному, то выводим ключ
