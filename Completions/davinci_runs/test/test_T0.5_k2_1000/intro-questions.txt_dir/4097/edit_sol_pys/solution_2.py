
def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        d = [b[i] - b[i - 1] for i in range(1, n)] + [b[0] - b[-1]]
        d.sort()
        if d[0] == d[-1]:
            print(0)
        else:
            print(2)

if __name__ == '__main__':
    main()
