
n, b, a = map(int, input().split())  # Ввод n, b, a
s = list(map(int, input().split()))  # Ввод списка s
max_segments = 0  # Инициализация переменной максимального количества сегментов
current_battery = b  # Инициализация переменной текущей зарядки батареи
current_accumulator = a  # Инициализация переменной текущего заряда аккумулятора
for i in range(n):  # Проход по последовательности
    if current_accumulator >= 1:  # Если заряд аккумулятора больше 1
        current_accumulator -= 1  # Уменьшаем заряд аккумулятора на 1
    else:  # Иначе
        current_battery -= 1  # Уменьшаем заряд батареи на 1
    if s[i] == 1:  # Если в списке по индексу i находится 1
        if current_battery < b:  # Если заряд батареи меньше максимального
            current_battery += 1  # Увеличиваем заряд батареи на 1
        else:  # Иначе
            current_accumulator += 1  # Увеличиваем заряд аккумулятора на 1
    max_segments += 1  # Увеличиваем переменную максимального количества сегментов на 1
    if current_battery == 0 and current_accumulator == 0:  # Если заряд батареи и аккумулятора равны 0
        break  # Прерываем цикл
print(max_segments)  # Выводим максимальное количество сегментов
