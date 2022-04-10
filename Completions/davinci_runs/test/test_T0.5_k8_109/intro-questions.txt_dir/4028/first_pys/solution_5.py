

import sys

def find_combinations(s):
    n = len(s)
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        if s[0] == '(' and s[1] == '(' and s[2] == ')':
            return 2
        return 0
    # n > 3
    if s[1] == '(' and s[-2] == ')':
        return find_combinations(s[1:-1])
    if s[0] == '(' and s[-1] == ')':
        return find_combinations(s[1:-1])
    return 0


def read_input():
    n = int(sys.stdin.readline())
    s = sys.stdin.readline().strip()
    return n, s


def solve(n, s):
    return find_combinations(s)


def main():
    n, s = read_input()
    print(solve(n, s))


if __name__ == "__main__":
    main()