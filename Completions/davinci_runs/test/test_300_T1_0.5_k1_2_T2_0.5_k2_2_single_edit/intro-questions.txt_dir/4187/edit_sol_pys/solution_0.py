

n = int(input('Введите количество элементов в массиве: '))
a = list(map(int, input('Введите массив: ').split()))

max_rest = 0
rest = 0

for i in a:
    if i == 0:
        max_rest = max(max_rest, rest)
        rest = 0
    else:
        rest += 1

max_rest = max(max_rest, rest)
print('Максимальное количество подряд идущих единиц: ', max_rest)
