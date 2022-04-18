

import math

def isPrime(n):
    if n == 1:
        return False
    for i in range(2, math.ceil(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def main():
    N = int(input())
    if isPrime(N):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()
