
import math


def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def find_minimum_prime(n):
    while not is_prime(n):
        n += 1
    return n


if __name__ == "__main__":
    x = int(input())
    print(find_minimum_prime(x))