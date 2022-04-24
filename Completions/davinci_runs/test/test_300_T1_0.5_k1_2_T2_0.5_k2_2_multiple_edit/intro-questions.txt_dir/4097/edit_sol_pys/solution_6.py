

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        print(1)
    else:
        d = [b[i] - b[i - 1] for i in range(1, n)]
        d.sort()
        if d[0] == d[-1]:
            print(0)
        else:
            print(0)

if __name__ == '__main__':
    main()
