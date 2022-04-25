#!/usr/bin/env python3

import math

def main():
    # Read input
    x = int(input(""))

    # Calculate minimum prime number that is larger than x
    prime_num = x
    while True:
        if is_prime(prime_num):
            break
        else:
            prime_num += 1

    # Output
    print(str(prime_num))

def is_prime(n):
    """
    Check if n is prime.
    """
    if n == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    main()
