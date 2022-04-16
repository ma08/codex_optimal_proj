

n, shuffle = input().split()  # ввод чисел
n = int(n)  # перевод строки в число

if shuffle == 'out':
    if n % 2 == 0:
        print(n // 2)
    else:
        print((n // 2) + 1)
else:
    if n % 2 == 0:
        print(n // 2)
    else:
        print(n // 2)
