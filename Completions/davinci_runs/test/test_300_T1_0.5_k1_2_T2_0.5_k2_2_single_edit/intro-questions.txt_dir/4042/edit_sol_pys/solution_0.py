

def main():
    x = float(input())

    for i in range(1, 100):
        for j in range(1, 10):
            if i / j == x:
                print(i, j)


if __name__ == '__main__':
    main()
