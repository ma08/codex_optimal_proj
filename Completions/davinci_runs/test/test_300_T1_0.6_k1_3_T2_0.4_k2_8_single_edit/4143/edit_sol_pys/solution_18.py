

def main():
    n, a, b, c, d, e = [int(input()) for i in range(6)]

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print(2)

if __name__ == '__main__':
    main()
