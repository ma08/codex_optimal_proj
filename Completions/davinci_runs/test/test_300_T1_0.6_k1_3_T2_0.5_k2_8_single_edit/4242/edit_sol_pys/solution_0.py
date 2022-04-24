

import math

def main():
    # Get inputs
    A, B, K = [int(input()) for _ in range(3)]

    # Get GCD and all divisors
    gcd = math.gcd(A, B)
    divisors = [d for d in range(1, gcd + 1) if gcd % d == 0]
    divisors.sort(reverse=True)

    # Print K-th largest positive integer that divides both A and B.
    print(divisors[K - 1])


if __name__ == '__main__':
    main()
