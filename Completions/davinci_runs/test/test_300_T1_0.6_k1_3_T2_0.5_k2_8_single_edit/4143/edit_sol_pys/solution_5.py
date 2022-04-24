

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    l = [a, b, c, d, e]
    l.sort()

    if n <= l[0]:
        print(1)
    else:
        print((n + l[0] - 1) // l[0] + 4)

if __name__ == '__main__':
    main()
