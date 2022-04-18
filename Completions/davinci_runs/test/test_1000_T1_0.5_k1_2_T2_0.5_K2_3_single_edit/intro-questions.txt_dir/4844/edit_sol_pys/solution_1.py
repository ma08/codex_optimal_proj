

def main():
    n = int(input())  # n - количество строк в матрице
    m = []  # матрица
    for i in range(n):  # считываем матрицу
        m.append([int(x) for x in input().split()])  # заполняем матрицу
    a = [0] * n  # создаем список a длиной n
    for i in range(n):  # перебираем строки матрицы
        for j in range(n):  # перебираем элементы строки
            if i != j:  # если элемент не стоит на главной диагонали
                a[i] = a[i] ^ m[i][j]  # применяем операцию XOR к элементу a[i] и m[i][j]
    print(*a)  # выводим список a

if __name__ == "__main__":
    main()
