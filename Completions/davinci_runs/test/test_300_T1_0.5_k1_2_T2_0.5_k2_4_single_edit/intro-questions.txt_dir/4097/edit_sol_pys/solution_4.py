

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    else:
        d = [b[i] - b[i - 1] for i in range(1, n)]
        if d[0] == 0:
            d[0] = d[1]
        d.sort()
        if d[0] == d[-1]:
            print(1)
        else:
            print(3)

if __name__ == '__main__':
    main()
