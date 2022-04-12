
h1, m1 = map(int, input().split(':')) # ввод времени
h2, m2 = map(int, input().split(':')) # ввод времени

m3 = (m1 + m2) // 2 # вычисление минут
h3 = h1 + (m1 + m2) // 120 # вычисление часов

if h3 > 23: # проверка на переход через полночь
    h3 -= 24 # вычитание 24 часов

print('{:02}:{:02}'.format(h3, m3))
