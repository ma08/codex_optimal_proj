

n, b, a = map(int, input().split())  # ввод данных
s = list(map(int, input().split()))  # ввод данных

max_segments = 0  # счетчик сегментов
cur_a = a
cur_b = b
for i in range(n):  # проходим по всем сегментам
    if s[i] == 1:
        if cur_b > 0:  # если есть батарейки
            cur_b -= 1
            cur_a += 1
            if cur_a > a:  # если аккумуляторов стало больше максимального числа
                cur_a = a
        else:  # если батареек нет, то заряжаем аккумулятор
            cur_a -= 1
    else:
        if cur_a > 0:  # если есть аккумуляторы
            cur_a -= 1
        else:  # если аккумуляторов нет, то заряжаем батарейки
            cur_b -= 1
    if cur_a == 0 and cur_b == 0:  # если нет заряда ни в аккумуляторах, ни в батарейках, то прекращаем цикл
        break
    max_segments += 1  # увеличиваем счетчик сегментов
print(max_segments)
