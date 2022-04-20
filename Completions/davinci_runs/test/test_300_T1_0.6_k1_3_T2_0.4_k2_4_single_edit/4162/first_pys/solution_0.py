

# N: The number of elements in a_i
# a_i: The elements in a_i

import sys

def read_input():
    """
    Reads in the input and parses it
    :return: N and a_i
    """
    N = int(sys.stdin.readline())
    a_i = list(map(int, sys.stdin.readline().split()))
    return N, a_i

def solve(N, a_i):
    """
    :param N: The number of elements in a_i
    :param a_i: The elements in a_i
    :return: The maximum value of f
    """
    # This is basically a greedy algorithm.
    # We want to maximize f(m) by making m as large as possible.
    # This is because f(m) = (m\ mod\ a_1) + (m\ mod\ a_2) + ... + (m\ mod\ a_N) is a linear function.
    # We want to maximize f(m) by making (m\ mod\ a_i) as large as possible for all a_i.
    # This is because (m\ mod\ a_i) = m - floor(m/a_i)*a_i.
    # Thus, m = (m\ mod\ a_i) + floor(m/a_i)*a_i.
    # To maximize m, we want to make floor(m/a_i) as large as possible, which is floor(m/a_i) = 1.
    # Thus, m = (m\ mod\ a_i) + a_i.
    # The largest value of (m\ mod\ a_i) is a_i - 1, so m = a_i - 1 + a_i = 2a_i - 1.
    # The sum of all the a_i is a_1 + a_2 + ... + a_N.
    # Thus, the maximum value of f(m) is f(m) = 2a_1 - 1 + 2a_2 - 1 + ... + 2a_N - 1 = 2(a_1 + a_2 + ... + a_N) - N = 2 * sum(a_i) - N
    return 2 * sum(a_i) - N

N, a_i = read_input()
print(solve(N, a_i))