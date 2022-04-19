

def main():
    x = float(input())

    for i in range(1, 10):  # TODO: переписать на цикл while
        for j in range(1, 10):  # TODO: переписать на цикл while
            if i / j == x:
                print(i, j)  # TODO: использовать форматирование строк
                break

if __name__ == '__main__':
    main()
