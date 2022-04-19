

x, y = map(int, input().split())  # чтение данных из консоли

if y % 2 == 0 and (2 * x + 4 * (y // 4 - x)) == y:  # проверка условия
    print('Yes')
else:
    print('No')
