

def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())  # n = number of rows, m = number of columns
        if n == 1:  # if there is only one row
            print(0)
        else:  # if there are more than one row
            print(max(2 * m - n, n - 2 * m))

if __name__ == '__main__':
    main()
