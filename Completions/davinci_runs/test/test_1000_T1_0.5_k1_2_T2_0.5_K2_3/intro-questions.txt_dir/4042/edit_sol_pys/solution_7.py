

def main():
    x = float(input('x: '))  # noqa

    for i in range(1, 10):
        for j in range(1, 10):
            if i / j == x:
                print(i, j)  # noqa

                break

if __name__ == '__main__':
    main()
