

a, b, c, d = map(int, input().split())  # считываем данные

if (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d):  # проверяем на пересечение
    print(b * d)  # выводим площадь пересечения
elif (c <= a <= d and a <= d <= b) or (a <= c <= b and c <= b <= d):  # проверяем на пересечение
    print(b * d)  # выводим площадь пересечения
elif (c <= a <= d and a <= b <= d) or (a <= c <= b and c <= d <= b):  # проверяем на пересечение
    print(b * d)  # выводим площадь пересечения
elif (a <= c <= b and c <= d <= b) or (c <= a <= d and a <= d <= b):  # проверяем на пересечение
    print(b * d)  # выводим площадь пересечения
else:
    print(a * c)  # выводим площадь
