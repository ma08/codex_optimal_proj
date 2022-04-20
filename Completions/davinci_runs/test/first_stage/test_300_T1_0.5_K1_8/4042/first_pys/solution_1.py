


def main():
    a = float(input())
    a = round(a, 6)
    for i in range(1, 10):
        for j in range(1, 10):
            if (i*j)/(i+j) == a:
                print(i, j)
                return

if __name__ == '__main__':
    main()