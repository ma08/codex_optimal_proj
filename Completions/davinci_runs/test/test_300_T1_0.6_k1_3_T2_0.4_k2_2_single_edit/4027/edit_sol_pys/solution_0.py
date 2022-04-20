def solve(n):
    if n == 1:
        return 1

    if n == 2:
        return 2

    if n == 3:
        return 3

    if n % 3 == 0:
        return solve(n - 1) + solve(n - 2)

    if n % 2 == 0:
        return solve(n - 1)

    return solve(n - 2)


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
