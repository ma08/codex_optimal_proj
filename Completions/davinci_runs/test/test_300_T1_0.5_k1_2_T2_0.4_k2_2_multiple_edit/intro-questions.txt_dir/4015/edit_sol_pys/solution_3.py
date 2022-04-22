
def get_input():
    return [int(x) for x in input().split()]


def solve(n, m):
    if n == m:
        return 0
    if n > m:
        return -1
    if m % n != 0:
        return -1
    return 1 + solve(n * 2, m) if m % (n * 2) == 0 else 1 + solve(n * 3, m)


if __name__ == '__main__':
    n, m = get_input()
    print(solve(n, m))
