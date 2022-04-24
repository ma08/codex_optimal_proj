

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, math.floor(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    for i in range(n):
        if is_prime(i) and is_prime(i + 6):
            print(i, i + 6)

if __name__ == "__main__":
    main()
