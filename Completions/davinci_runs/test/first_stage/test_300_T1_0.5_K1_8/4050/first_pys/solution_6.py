

n = int(input())
a = list(map(int, input().split()))

# создаем массив для хранения данных о префиксных суммах
# префиксная сумма последовательности элементов a[0], a[1], ..., a[i] равна
# a[0] + a[1] + ... + a[i]
prefix_sum = [0] * (n + 1)
for i in range(1, n + 1):
    prefix_sum[i] = prefix_sum[i - 1] + a[i - 1]

# для каждой пары индексов (l, r) сохраняем количество блоков, которые можно составить из последовательности элементов a[l], a[l + 1], ..., a[r]
# по умолчанию это количество равно 0
count = [[0] * (n + 1) for _ in range(n + 1)]

# для каждой пары индексов (l, r) сохраняем предыдущий индекс, при котором для последовательности элементов a[l], a[l + 1], ..., a[r]
# было найдено максимальное количество блоков
prev = [[0] * (n + 1) for _ in range(n + 1)]

# перебираем все пары индексов (l, r)
for l in range(n - 1, -1, -1):
    for r in range(l + 1, n + 1):
        # находим префиксную сумму последовательности элементов a[l], a[l + 1], ..., a[r]
        s = prefix_sum[r] - prefix_sum[l]
        # перебираем все индексы между l и r
        for i in range(l + 1, r):
            # если префиксная сумма последовательности элементов a[l], a[l + 1], ..., a[i] равна префиксной сумме последовательности элементов a[i + 1], a[i + 2], ..., a[r]
            if prefix_sum[i] - prefix_sum[l] == prefix_sum[r] - prefix_sum[i]:
                # увеличиваем количество блоков на 1
                count[l][r] = count[l][i] + count[i][r] + 1
                # сохраняем предыдущий индекс
                prev[l][r] = i
                break

# находим пару индексов (l, r), для которой было найдено максимальное количество блоков
max_l, max_r = 0, 0
for l in range(n):
    for r in range(l + 1, n + 1):
        if count[l][r] > count[max_l][max_r]:
            max_l, max_r = l, r

# выводим количество блоков
print(count[max_l][max_r] + 1)

# выводим блоки
while max_l < max_r:
    print(max_l + 1, max_r)
    max_l, max_r = prev[max_l][max_r], max_l