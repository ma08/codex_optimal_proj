
x = int(input())  # вводим год
if x % 4 == 0 and x % 100 != 0 or x % 400 == 0:  # проверяем является ли год високосным
    print('YES')
else:
    print('NO')
