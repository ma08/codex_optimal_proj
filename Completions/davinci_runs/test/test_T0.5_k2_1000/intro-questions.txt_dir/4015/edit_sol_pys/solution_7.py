

def get_input():
    return [int(x) for x in input().split()][0]


def solve(a, b):
    if a == b:
        return 0
    if a > b:
        return -1
    if b % a != 0:
        return -1
    return solve(a * 2, b) + 1 if b % (a * 2) == 0 else solve(a * 3, b) + 1


if __name__ == '__main__':
    a = get_input()
    b = get_input()
    print(solve(a, b))
