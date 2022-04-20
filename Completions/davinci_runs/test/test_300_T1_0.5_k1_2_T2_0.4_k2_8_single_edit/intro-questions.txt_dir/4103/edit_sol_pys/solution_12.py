

n, b, a = map(int, input().split())  # n - количество сегментов, b - количество батарей, a - количество аккумуляторов
s = list(map(int, input().split()))  # массив сегментов

max_segments = 0  # количество пройденных сегментов
current_battery = b  # количество батарей
current_accumulator = a  # количество аккумуляторов
for i in range(n):
    if current_accumulator >= 1:  # если есть аккумуляторы
        current_accumulator -= 1  # используем аккумуляторы
    else:
        current_battery -= 1  # иначе используем батареи
    if s[i] == 1:  # если сегмент без солнца
        if current_battery < b:  # если не полностью заряжены батареи
            current_battery += 1  # заряжаем батареи
        else:
            current_accumulator += 1  # иначе заряжаем аккумуляторы
    max_segments += 1  # проходим сегмент
    if current_battery == 0 and current_accumulator == 0:  # если закончились батареи и аккумуляторы
        break

print(max_segments)
