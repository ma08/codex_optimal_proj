def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        c = [b[i] - b[i - 1] for i in range(1, n)]
        c.sort()
        if c[0] == c[-1]:
            print(0)
        else:
            print(2)

if __name__ == '__main__':
    main()
