
def main():
    x = float(input())  # дробное число

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(i, j)  # вывод найденных чисел

                break

if __name__ == '__main__':
    main()
