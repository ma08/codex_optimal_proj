

def main():
    x = float(input())

    for i in range(1, 10):
        j = x * i
        if j % 1 == 0:
            print(i, int(j))


if __name__ == '__main__':
    main()
