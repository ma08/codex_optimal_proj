

import sys import math

def isPrime(n):
    if n <= 1:
        return False
    i = 2
    while i <= math.sqrt(n):
        if n % i == 0:
            return False
        i += 1
    return True

def main():
    n = int(sys.stdin.readline().strip())
    for i in range(n+1, 1000):
        if (i % 111 == 0) and isPrime(i):
            print(i)
            break

if __name__ == "__main__":
    main()
