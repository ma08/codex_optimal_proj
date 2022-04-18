

n, k = map(int, input().split())  # ввод данных

segments = []  # создание массива для отрезков

for _ in range(n):  # ввод отрезков
    segments.append(tuple(map(int, input().split())))  # запись отрезков в массив

# print(segments)

segments.sort()  # сортировка отрезков по левой границе

# print(segments)

result = []  # создание массива для результатов

for i in range(n):  # пробегаемся по всем отрезкам
    l, r = segments[i]  # получаем левую и правую границу текущего отрезка
    j = i + 1  # начинаем проверку со следующего отрезка
    while j < n and segments[j][0] <= r:  # проверяем, попадает ли отрезок в границы текущего отрезка
        if segments[j][1] > r:  # если да, то проверяем, не больше ли правая граница текущего отрезка
            r = segments[j][1]  # если да, то обновляем правую границу
        j += 1  # переходим к следующему отрезку
    result.append((r - l + 1, i))  # добавляем длину отрезка и его номер в массив результатов

# print(result)

result.sort(reverse=True)  # сортируем массив результатов по убыванию длины отрезка

# print(result)

result = [i + 1 for _, i in result]  # получаем массив с номерами отрезков с учетом длины

# print(result)

cnt = 0

for i in result:
    l, r = segments[i]
    if cnt + r - l + 1 <= k:
        cnt += r - l + 1
    else:
        break

print(len(result) - cnt)
print(*result[:len(result) - cnt])
