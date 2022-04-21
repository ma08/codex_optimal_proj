

def main():
    x = float(input())

    for i in range(1, 10):  # noqa
        for j in range(1, 10):  # noqa
            if i / j == x:
                print(i, j)
                break

if __name__ == '__main__':
    main()
