

def get_input():
    return [int(x) for x in input().split()]  # noqa: E501


def solve(n, m):
    if n == m:  # noqa: E501
        return 0
    if n > m:  # noqa: E501
        return -1
    if m % n != 0:  # noqa: E501
        return -1
    return solve(n * 2, m) + 1 if m % (n * 2) == 0 else solve(n * 3, m) + 1  # noqa: E501


if __name__ == '__main__':
    n, m = get_input()
    print(solve(n, m))
