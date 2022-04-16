

import sys
import math

def main():

    x = int(sys.stdin.readline())

    print(num_primes(x))


def num_primes(x):

    num_primes = 0

    if x == 1:
        return 0

    while x > 1:

        if x % 2 == 0:
            x = x // 2

        else:
            factor = smallest_odd_factor(x)

            x = x // factor

        num_primes += 1

    return num_primes


def smallest_odd_factor(x):

    smallest_odd_factor = x

    for i in range(3,int(math.sqrt(x)+1),2):

        if x % i == 0:

            smallest_odd_factor = i

            break

    return smallest_odd_factor


if __name__ == "__main__":
    main()
