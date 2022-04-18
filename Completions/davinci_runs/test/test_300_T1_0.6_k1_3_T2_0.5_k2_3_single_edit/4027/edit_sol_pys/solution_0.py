def solve(n):
    if n % 2 == 0:
        return 0
    return 1


if __name__ == '__main__':
    n = int(input())
    print(solve(n))
