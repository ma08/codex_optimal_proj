

def main():
    x = float(input())  # Находим делитель и делимое

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(i, j)  # Выводим делитель и делимое
                break

if __name__ == '__main__':
    main()
