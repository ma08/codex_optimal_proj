
n, m = map(int, input().split())  # количество отрезков и точек

segments = []  # список отрезков
for i in range(n):
    l, r = map(int, input().split())
    segments.append((l, r))  # добавление отрезка в список

segments.sort(key=lambda x: x[0])  # сортировка отрезков по левой границе

print(segments)

res = []  # список непокрытых точек
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:  # проверка на покрытие
        res.append(i)  # добавление непокрытой точки в список

print(len(res))  # количество непокрытых точек
print(*res)  # вывод непокрытых точек
