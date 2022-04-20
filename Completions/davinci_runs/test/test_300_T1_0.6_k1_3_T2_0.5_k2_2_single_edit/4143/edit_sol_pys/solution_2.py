

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    l = sorted([a, b, c, d, e])

    print(-(-(n + l[0] - 1) // l[0]))

if __name__ == '__main__':
    main()
