
def get_input():
    return [int(x) for x in input().split()]


def solve(n):
    if n % 2 == 0:
        return solve(n // 2)
    if n % 3 == 0:
        return solve(n // 3)
    if n % 5 == 0:
        return solve(n // 5)
    return n == 1


if __name__ == '__main__':
    n = get_input()[0]
    print('YES' if solve(n) else 'NO')
