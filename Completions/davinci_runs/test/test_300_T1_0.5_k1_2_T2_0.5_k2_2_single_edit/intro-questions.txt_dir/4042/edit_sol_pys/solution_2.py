
def main():
    x = float(input())  # вводимое число

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:  # делим пары чисел и сравниваем с введенным
                print(i, j)  # если совпадает, выводим пару чисел
                break  # и прекращаем перебор


if __name__ == '__main__':
    main()
