

# n = 5
# m = 4
# a = [2, 4, 5, 3, 1]

n, m = map(int, input().split())
a = list(map(int, input().split()))

# a = [1, 2, 3, 4, 5]
# a = [1, 15, 2, 14, 3, 13, 4, 8, 12, 5, 11, 6, 10, 7, 9]

# m = 5
# m = 8

# Считаем число перестановок таких, что медиана не совпадает с m

# Перестановки без медианы
# Найдем медиану. Если она не в середине, то перестановок не будет
# Если она в середине, то перестановок будет столько, сколько элементов меньше медианы и столько, сколько элементов больше медианы
# Всего будет на 1 больше, так как вариант не переставлять ничего

# Перестановки с медианой
# Найдем медиану. Если она не в середине, то перестановок не будет
# Если она в середине, то перестановок будет столько, сколько элементов меньше медианы и столько, сколько элементов больше медианы
# Всего будет на 1 больше, так как вариант не переставлять ничего

# Получается, что нужно вычесть из перестановок без медианы те, где медиана в середине

# Заполним число перестановок слева и справа от каждого элемента

# Слева

# Будем заполнять слева от каждого элемента
# Пусть мы находимся на элементе a[i]
# Если a[i] меньше медианы, то перестановок будет всего элементов слева от него
# Если a[i] больше медианы, то перестановок не будет

# Справа

# Будем заполнять справа от каждого элемента
# Пусть мы находимся на элементе a[i]
# Если a[i] больше медианы, то перестановок будет всего элементов справа от него
# Если a[i] меньше медианы, то перестановок не будет

# Получается, что нужно вычесть из суммы числа перестановок слева и справа от медианы те, где медиана в середине

# Найдем медиану
median = sorted(a)[n // 2]

# Найдем количество перестановок без медианы
# Заполним число перестановок слева и справа от каждого элемента

# Слева

# Будем заполнять слева от каждого элемента
# Пусть мы находимся на элементе a[i]
# Если a[i] меньше медианы, то перестановок будет всего элементов слева от него
# Если a[i] больше медианы, то перестановок не будет

# Справа

# Будем заполнять справа от каждого элемента
# Пусть мы находимся на элементе a[i]
# Если a[i] больше медианы, то перестановок будет всего элементов справа от него
# Если a[i] меньше медианы, то перестановок не будет

# Получается, что нужно вычесть из суммы числа перестановок слева и справа от медианы те, где медиана в середине

# Слева
left = [0] * n

for i in range(n):
    if a[i] < median:
        left[i] = i
    else:
        left[i] = 0

# Справа
right = [0] * n

for i in range(n - 1, -1, -1):
    if a[i] > median:
        right[i] = n - i - 1
    else:
        right[i] = 0

# Сумма
sum = 0

for i in range(n):
    sum += left[i] + right[i]

# Уменьшим на те, где медиана в середине
sum -= left[n // 2] + right[n // 2]

# Найдем количество перестановок с медианой
# Заполним число перестановок слева и справа от каждого элемента

# Слева
left = [0] * n

for i in range(n):
    if a[i] < median:
        left[i] = i
    else:
        left[i] = 0

# Справа
right = [0] * n

for i in range(n - 1, -1, -1):
    if a[i] > median:
        right[i] = n - i - 1
    else:
        right[i] = 0

# Сумма
sum_median = 0

for i in range(n):
    sum_median += left[i] + right[i]

# Уменьшим на те, где медиана в середине
sum_median -= left[n // 2] + right[n // 2]

# Вычтем перестановки с медианой из перестановок без медианы
print(sum - sum_median)
