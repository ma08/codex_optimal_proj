

def main():
    n = int(input()) - 1
    a = int(input()) - 1
    b = int(input()) - 1
    c = int(input()) - 1
    d = int(input()) - 1
    e = int(input()) - 1

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0] * 5:
        print(1)
    else:
        print((n + l[0] - 1) // l[0] + 4)

if __name__ == '__main__':
    main()
