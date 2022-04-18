
def main():
    x = float(input('x: '))

    i = 1
    j = 1
    while i <= 10:
        while j <= 10:
            if i / j == x: print(i, j)
            j += 1
        i += 1


if __name__ == '__main__':
    main()
