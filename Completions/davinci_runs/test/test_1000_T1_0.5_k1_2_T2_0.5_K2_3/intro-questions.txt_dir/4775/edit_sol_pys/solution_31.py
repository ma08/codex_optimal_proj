
a, b = input().split()  # разбиваем на две строки по пробелу
N, M = len(a), len(b)  # получаем длину строк

for i in range(M):  # цикл по длине строки b
    for j in range(N):  # цикл по длине строки a
        if a[j] == b[i]:  # если символы совпадают
            print(b[i], end='')
        else:  # если нет
            print('.', end='')
    print()
