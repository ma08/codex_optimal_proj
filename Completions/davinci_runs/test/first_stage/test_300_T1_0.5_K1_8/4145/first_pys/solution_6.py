
import math

def is_prime(n):
    """
    Check if a number is prime.
    """
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def main():
    """
    Main function.
    """
    x = int(input())
    while not is_prime(x):
        x += 1
    print(x)

if __name__ == '__main__':
    main()