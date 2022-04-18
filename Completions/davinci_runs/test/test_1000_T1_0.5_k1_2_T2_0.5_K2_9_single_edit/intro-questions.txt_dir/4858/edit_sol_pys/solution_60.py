

def main():
    M, N, C = input().split()  # считываем первую строку
    M = int(M)
    N = int(N)
    first = []  # пустой список для первого массива
    second = []  # пустой список для второго массива
    for i in range(M):
        first.append(list(input()))  # считываем первый массив
    for i in range(M):
        second.append(list(input()))  # считываем второй массив
    for i in range(M):
        for j in range(N):
            if first[i][j] != C:  # если элемент первого массива не равен цвету
                first[i][j] = '.'  # заменяем его на точку
            else:
                first[i][j] = 'X'  # иначе заменяем на X
            if second[i][j] != C:  # если элемент второго массива не равен цвету
                second[i][j] = '.'  # заменяем его на точку
            else:
                second[i][j] = 'X'  # иначе заменяем на X
    for i in range(M):
        for j in range(N):
            if second[i][j] == 'X' and first[i][j] != 'X':  # если элемент второго массива равен X, а первого нет
                second[i][j] = '^'  # заменяем этот элемент на каретку
    for i in range(M):
        for j in range(N):
            if second[i][j] == '^':  # если элемент второго массива равен каретке
                second[i][j] = '.'  # заменяем его на точку
            if second[i][j] == 'X':  # если элемент второго массива равен X
                second[i][j] = C  # заменяем его на цвет
    for i in range(M):
        print(''.join(second[i]))  # выводим второй массив
    print()  # переносим курсор на новую строку

if __name__ == '__main__':
    main()
