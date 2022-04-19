
import math
import sys

def is_hard_to_enter(code):
    """
    Returns True if the code is hard to enter, False otherwise.
    """
    for i in range(len(code) - 1):
        if code[i] == code[i+1]:
            return True
    return False
def is_prime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def prime_divisors(n):
    divisors = []
    for i in range(2, n + 1):
        if n % i == 0 and is_prime(i):
            divisors.append(i)
    return divisors


def main():
    n = int(sys.stdin.readline().rstrip())
    divisors = prime_divisors(n)
    print(" ".join(map(str, divisors)))

if __name__ == "__main__":
    main()
