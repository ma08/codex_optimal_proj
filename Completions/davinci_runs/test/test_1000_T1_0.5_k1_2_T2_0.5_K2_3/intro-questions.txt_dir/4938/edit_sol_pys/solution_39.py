
X = int(input())
line = input()

women = men = 0 # Количество женщин и мужчин

for person in line: # Проходим по всем людям
    if person == 'W':
        women += 1
    else:
        men += 1

    if abs(women - men) > X: # Если количество женщин и мужчин отличается больше чем на X, то выходим
        break

print(women + men) # Выводим сумму женщин и мужчин
