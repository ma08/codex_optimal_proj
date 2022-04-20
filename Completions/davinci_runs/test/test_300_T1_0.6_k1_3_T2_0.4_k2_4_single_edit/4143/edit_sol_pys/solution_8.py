

def main():
    n = int(input())
    a = int(input())
    b = int(input())
    c = int(input())
    d = int(input())
    e = int(input())

    l = sorted([a, b, c, d, e])

    print(5 if n <= l[0] else 4)

if __name__ == '__main__':
    main()
