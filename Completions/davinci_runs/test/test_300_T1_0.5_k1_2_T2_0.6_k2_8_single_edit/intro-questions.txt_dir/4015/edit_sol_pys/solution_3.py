

def get_input():
    return [int(x) for x in input().split()]


def solve(n):
    if n == 1:
        return 1
    return solve(n // 2) + 1 if n % 2 == 0 else solve(n // 3) + 1


if __name__ == '__main__':
    n = get_input()[0]
    print(solve(n))
