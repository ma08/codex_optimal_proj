

n, m = map(int, input().split())  # n - кол-во отрезков, m - кол-во точек

segments = []  # список отрезков
for i in range(n):
    left, right = map(int, input().split())
    segments.append((left, right))  # добавляем в список отрезки

segments.sort(key=lambda x: x[0])  # сортируем по левой стороне отрезка

# print(segments)  # для проверки

res = []  # список для ответа
for i in range(1, m + 1):
    if i not in [seg[0] for seg in segments] and i not in [seg[1] for seg in segments]:  # проверка на принадлежность точки к отрезку
        res.append(i)  # добавляем в список ответа

print(len(res))  # выводим кол-во точек
print(*res)  # выводим точки
