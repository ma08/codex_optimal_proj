
def main():
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())  # split the input
        if n == 1:
            print(0)  # if n is 1
        else:
            print(max(2 * m - n, n - 2 * m))  # otherwise


if __name__ == '__main__':
    main()
