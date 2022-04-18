
def main():
    x = float(input())

    for i in range(1, 10):  # перебор чисел от 1 до 9
        for j in range(1, 10):  # перебор чисел от 1 до 9
            if i / j == x:
                print(i, j)
                break  # прерываем внутренний цикл


if __name__ == '__main__':
    main()
