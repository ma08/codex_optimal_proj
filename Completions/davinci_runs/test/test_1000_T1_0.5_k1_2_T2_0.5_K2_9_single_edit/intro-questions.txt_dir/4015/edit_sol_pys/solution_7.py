
def get_input():
    return [int(x) for x in input().split()][0]


def solve(n, m):
    return 0 if n == m else -1 if n > m or m % n != 0 else solve(n * 2, m) + 1 if m % (n * 2) == 0 else solve(n * 3, m) + 1


if __name__ == '__main__':
    n, m = get_input()
    print(solve(n, m))
