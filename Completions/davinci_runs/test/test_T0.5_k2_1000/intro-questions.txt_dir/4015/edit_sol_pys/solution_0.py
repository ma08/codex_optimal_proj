
def get_input():
    return [int(x) for x in input().split()]  # read a list of integers, 2 in this case


def solve(a, b):
    if a == b:  # equal
        return 0
    if a > b:  # impossible to generate
        return -1
    if b % a != 0:  # impossible to generate
        return -1
    return solve(a * 2, b) + 1 if b % (a * 2) == 0 else solve(a * 3, b) + 1  # either of them is ok


if __name__ == '__main__':
    n, m = get_input()
    print(solve(n, m))
