

def main():
    x = float(input())  # Число для поиска

    for i in range(1, 10):  # Перебираем все числа от 1 до 9
        for j in range(1, 10):  # Перебираем все числа от 1 до 9
            if i / j == x:  # Если деление соответствует числу для поиска
                print(i, j)  # Выводим числа
                break

if __name__ == '__main__':
    main()
