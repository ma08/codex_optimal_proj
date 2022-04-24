

def get_input():
    return [int(x) for x in input().split()]


def solve(a, b):
    if a == b:
        return 0
    if a > b:
        return -1
    if b % a != 0:
        return -1
    return solve(a * 2, b) + 1 if b % (a * 2) == 0 else solve(a * 3, b) + 1


if __name__ == '__main__':
    n, m = get_input()
    print(solve(n, m))
