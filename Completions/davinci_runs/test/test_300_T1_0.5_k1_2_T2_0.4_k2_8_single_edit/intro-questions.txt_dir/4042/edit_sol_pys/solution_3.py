
def main():
    x = float(input())

    for i in range(1, 10):    # Цикл для делимого
        for j in range(1, 10):    # Цикл для делителя
            if i / j == x:    # Если деление дает результат x, то выводим на экран
                print(i, j)    # Вывод на экран
                break    # Выход из цикла


if __name__ == '__main__':
    main()
