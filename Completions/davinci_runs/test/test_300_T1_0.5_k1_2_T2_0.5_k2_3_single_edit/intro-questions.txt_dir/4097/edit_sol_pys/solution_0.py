


def solve(n, b):
    d = [b[i] - b[i - 1] for i in range(1, n)]
    d.sort()
    if d[0] == d[-1]:
        return 0
    else:
        return 2


def main():
    n = int(input())
    b = [int(x) for x in input().split()]
    if n == 1:
        print(0)
    elif n == 2:
        print(0)
    else:
        print(solve(n, b))

if __name__ == '__main__':
    main()
