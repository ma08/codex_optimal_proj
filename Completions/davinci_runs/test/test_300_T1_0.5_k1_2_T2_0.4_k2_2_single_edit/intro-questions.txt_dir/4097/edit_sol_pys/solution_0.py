

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        d = [b[i] - b[i - 1] for i in range(1, n)]  # difference between consecutive elements
        d.sort()
        if d[0] == d[-1]:  # if all elements are equal
            print(0)
        else:
            print(2)  # if all elements are not equal


if __name__ == '__main__':
    main()
