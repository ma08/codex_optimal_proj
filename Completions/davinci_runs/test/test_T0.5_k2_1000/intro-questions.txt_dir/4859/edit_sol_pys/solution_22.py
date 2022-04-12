

from itertools import product

b, d, c, l = map(int, input().split())  # ввод данных и преобразование в целочисленный тип

for i, j, k in product(range(l//b + 1), range(l//d + 1), range(l//c + 1)):  # перебор всех возможных вариантов
    if i*b + j*d + k*c == l:  # проверка на соответствие
        print(i, j, k)
