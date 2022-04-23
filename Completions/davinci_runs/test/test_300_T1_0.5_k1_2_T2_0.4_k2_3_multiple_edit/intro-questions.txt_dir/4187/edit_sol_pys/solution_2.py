
n = int(input())
a = list(map(int, input().split()))

max_rest = 0
rest = 0

for i in a:  # проходим по всем элементам массива
    if i == 0:  # если элемент равен 0
        max_rest = max(max_rest, rest)
        rest = 0  # обнуляем счетчик подряд идущих единиц
    else:  # если элемент не равен 0
        rest += 1  # увеличиваем счетчик подряд идущих единиц

max_rest = max(max_rest, rest)
print(max_rest)
