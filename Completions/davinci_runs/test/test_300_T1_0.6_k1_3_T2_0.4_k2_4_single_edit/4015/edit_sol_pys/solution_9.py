

def solve(n, m):
    if n == m:
        return 0

    if m % 2 == 1 and m % 3 == 1:
        return -1

    steps = 0

    while n != 1:
        if n % 3 == 0:
            n = int(n / 3)
        elif n % 2 == 0:
            n = int(n / 2)
        else:
            return -1
        steps += 1

    while m != 1:
        if m % 3 == 0:
            m = int(m / 3)
        elif m % 2 == 0:
            m = int(m / 2)
        else:
            return -1
        steps += 1

    return steps


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(solve(n, m))
