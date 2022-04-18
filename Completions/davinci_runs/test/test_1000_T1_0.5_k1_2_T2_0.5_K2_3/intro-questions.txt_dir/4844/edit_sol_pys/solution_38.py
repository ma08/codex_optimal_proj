

def main():
    n = int(input())
    i = 0
    j = 0
    arr = []
    while i < n:
        arr.append(list(map(int, input().split())))  # получаем матрицу
        i += 1
    res = [0] * n  # инициализируем массив результата
    while j < n:
        res[j] = arr[j][0]
        j += 1
    i = 1
    while i < n:
        res[i] = arr[0][i]
        i += 1
    i = 1
    while i < n:
        j = 1
        while j < n:
            if i != j:  # если это не диагональный элемент
                res[i] = res[i] ^ arr[i][j]  # добавляем в массив результата
            j += 1
        i += 1
    print(*res)

if __name__ == "__main__":
    main()
