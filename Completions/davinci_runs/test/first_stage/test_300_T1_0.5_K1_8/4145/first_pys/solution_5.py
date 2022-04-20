
import math

def isPrime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    X = int(input())
    while isPrime(X) == False:
        X += 1
    print(X)

if __name__ == '__main__':
    main()