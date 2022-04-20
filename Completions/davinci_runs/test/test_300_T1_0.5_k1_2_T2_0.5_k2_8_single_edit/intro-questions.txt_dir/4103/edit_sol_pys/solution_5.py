

n, b, a = map(int, input().split())  # количество сегментов, количество полных аккумуляторов, количество полных батарей
s = list(map(int, input().split()))  # последовательность сегментов

max_segments = 0  # количество пройденных сегментов
current_battery = b  # количество батарей
current_accumulator = a  # количество аккумуляторов
for i in range(n):
    if current_accumulator >= 1:  # если есть аккумуляторы, то происходит зарядка
        current_accumulator -= 1  # тратим аккумулятор
    else:
        current_battery -= 1  # тратим батарею
    if s[i] == 1:  # если на сегменте есть станция зарядки
        if current_battery < b:  # если батарей меньше, чем должно быть
            current_battery += 1  # заряжаем батарею
        else:
            if current_accumulator > a:  # если аккумуляторов больше, чем должно быть
                current_accumulator = a  # ограничиваем количество аккумуляторов
    max_segments += 1  # увеличиваем количество пройденных сегментов
    if current_battery == 0 and current_accumulator == 0:  # если нет батарей и аккумуляторов
        break

print(max_segments)
