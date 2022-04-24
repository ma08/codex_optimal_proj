

import math

import numpy as np


def get_factors(n):
    factors = set()
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors


def main():
    N = int(input())
    A = np.array([int(x) for x in input().split(' ')])

    factors = get_factors(N)
    for factor in factors:
        # print(factor)
        for i in range(0, N, factor):
            if i + factor >= N:
                break
            A[i:i + factor] = A[i:i + factor][::-1]
        # print(A)
    print(' '.join(map(str, A)))


if __name__ == "__main__":
    main()
