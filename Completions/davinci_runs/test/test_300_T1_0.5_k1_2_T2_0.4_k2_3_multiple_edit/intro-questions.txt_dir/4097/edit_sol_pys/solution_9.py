
def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        print(0)
    else:
        d = sorted([b[i] - b[i - 1] for i in range(1, n)])
        if d[0] == d[-1] or (d[0] == d[-2] and d[-1] == 2 * d[0]):
            print(0)
        else:
            print(2)

if __name__ == '__main__':
    main()
