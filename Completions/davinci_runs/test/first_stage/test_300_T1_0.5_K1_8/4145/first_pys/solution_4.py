

import math

def is_prime(n):
    if n < 2:
        return False
    # Only need to check up to the square root of n.
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    # Get input.
    x = int(input())
    # If x is prime, return it.
    if is_prime(x):
        print(x)
    else:
        # Iterate up until we find the next prime number.
        while not is_prime(x):
            x += 1
        print(x)

if __name__ == "__main__":
    main()