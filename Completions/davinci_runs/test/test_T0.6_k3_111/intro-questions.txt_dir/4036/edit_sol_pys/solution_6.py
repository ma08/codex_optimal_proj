
n, k = map(int, input().split())  # ввод данных

if n == 1:  # если введено 1
    print("YES")
    print("1")
elif n > 2 * (2 ** (k - 1) - 1) or n < 2 ** (k - 1):  # если введено неверное количество
    print("NO")
else:  # если введено верное количество
    print("YES")
    for i in range(k - 1):  # вывод первых k-1 чисел
        print(2 ** (k - i - 1) - 1, end=' ')

    if n - (2 ** (k - 1) - 1) == 2 ** (k - 1):  # вывод последнего числа
        print(2 ** (k - 1))
    else:
        print(n - (2 ** (k - 1) - 1))
