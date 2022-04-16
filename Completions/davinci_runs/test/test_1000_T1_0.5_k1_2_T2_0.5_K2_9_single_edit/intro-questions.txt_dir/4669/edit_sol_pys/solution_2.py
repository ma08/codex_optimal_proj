

import math

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            return False
    return True

def main():
    n = int(input())
    if is_prime(n):
        print("Prime")
    else:
        print("Not prime")

if __name__ == '__main__':
    main()
