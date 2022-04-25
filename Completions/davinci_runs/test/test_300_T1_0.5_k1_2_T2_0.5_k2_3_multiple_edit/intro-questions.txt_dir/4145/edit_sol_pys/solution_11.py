
import math

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n <= 1:
        return False

    sqr = int(math.sqrt(n))

    for divisor in range(3, sqr, 2):
        if n % divisor == 0:
            return False
    return True

def main():
    X = int(input())
    while(True):
        if is_prime(X):
            print(X)
            break
        X += 1

if __name__ == '__main__':
    main()
