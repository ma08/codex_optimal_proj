def main():
    n, m = map(int, input().split())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    if a + c > n:
        print(-1)
    else:
        if b < d:
            if b + d > m:
                print(-1)
            else:
                print(a, b+d)
                print(c, d)
        else:
            if b + d > m:
                print(-1)
            else:
                print(a, b)
                print(c, d+b)


if __name__ == '__main__':
    main()
