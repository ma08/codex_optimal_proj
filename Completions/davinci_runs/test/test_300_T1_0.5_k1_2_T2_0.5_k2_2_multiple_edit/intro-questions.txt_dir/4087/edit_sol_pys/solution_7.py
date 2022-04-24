

def main():
    a = int(input())  # вводим число
    while True:
        if a % 4 == 0:  # проверяем делится ли оно нацело на 4
            print(a)  # выводим на экран
            break
        else:
            a += 1  # прибавляем 1


if __name__ == '__main__':
    main()
