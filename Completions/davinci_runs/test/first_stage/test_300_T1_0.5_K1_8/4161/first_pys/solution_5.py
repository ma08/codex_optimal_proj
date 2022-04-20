


def gcd3(a, b, c):
    return gcd(gcd(a, b), c)


def solve(k):
    return sum(gcd3(a, b, c) for a in range(1, k + 1) for b in range(1, k + 1) for c in range(1, k + 1))


def main():
    k = int(input().rstrip())
    print(solve(k))


if __name__ == '__main__':
    main()