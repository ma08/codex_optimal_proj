

# TODO


def solve(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + solve(n / 2)
    if n % 3 == 0:
        return 1 + solve(2 * n / 3)
    if n % 5 == 0:
        return 1 + solve(4 * n / 5)
    return -1


def main():
    q = int(input())
    for _ in range(q):
        n = int(input())
        print(solve(n))


if __name__ == '__main__':
    main()
