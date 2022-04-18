#!/usr/bin/env python3

import sys


def solve(N: int, a: int, b: int):
    return 0


def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    N = int(next(tokens))  # type: int
    a = int(next(tokens))  # type: int
    b = int(next(tokens))  # type: int
    result = solve(N, a, b)
    print(result)


if __name__ == '__main__':
    main()


n, a, b = map(int, read().split())

# The pattern is repeated every (a + b) balls.
# We can find our answer by finding the remainder of n / (a + b)
# and counting the number of blue balls in that pattern.
n = n % (a + b)

# If we don't have enough balls to fill out a pattern,
# we can simply count the number of blue balls we have.
if n <= a:
    print(n)
else:
    # Otherwise, count the number of blue balls in the last pattern.
    print(a)
