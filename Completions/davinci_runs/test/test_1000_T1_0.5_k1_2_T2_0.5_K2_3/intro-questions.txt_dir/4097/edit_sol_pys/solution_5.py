

    a = [int(x) for x in input().split()]
def main():
    n = int(input())
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        d = [a[i] - a[i - 1] for i in range(1, n)]
        d.sort()
        if d[0] == d[-1]:
            print(0)
        else:
            print(2)

if __name__ == '__main__':
    main()
