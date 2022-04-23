

def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(1)
    elif n == 2:
        print(0)
    else:
        d = [b[i] - b[i - 1] for i in range(1, n)]  # d is a list of differences
        d.sort()  # sort the list
        if d[0] == d[-1]:  # if the smallest difference is the same as the largest difference
            print(0)
        else:  # otherwise
            print(2)

if __name__ == '__main__':
    main()
