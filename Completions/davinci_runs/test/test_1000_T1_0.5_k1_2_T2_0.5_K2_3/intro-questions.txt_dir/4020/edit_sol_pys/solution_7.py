
h1, m1 = map(int, input().split(':')) # Вводим первое время
h2, m2 = map(int, input().split(':')) # Вводим второе время

m3 = (m1 + m2) // 2 # Получаем минуты между временем
h3 = h1 + (m1 + m2) // 120 # Получаем часы между временем

if h3 > 23: # Если получилось больше 23 часов, то отнимаем 24
    h3 -= 24

print('{:02}:{:02}'.format(h3, m3)) # Выводим время с двумя нулями
