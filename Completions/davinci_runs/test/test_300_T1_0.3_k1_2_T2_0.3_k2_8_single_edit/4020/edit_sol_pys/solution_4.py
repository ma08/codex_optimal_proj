

h1, m1 = input().split(':') # ввод первого времени
h2, m2 = input().split(':') # ввод второго времени

h1 = int(h1) # перевод первого часа в целое число
m1 = int(m1) # перевод первой минуты в целое число
h2 = int(h2) # перевод второго часа в целое число
m2 = int(m2) # перевод второй минуты в целое число

if m1 == m2:
    if h1 == h2:
        print(str(h1).zfill(2) + ':' + str(m1).zfill(2))
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(m1).zfill(2))
else:
    if h1 == h2:
        print(str(h1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
    else:
        print(str(h1 + 1).zfill(2) + ':' + str(int((m1 + m2) / 2)).zfill(2))
