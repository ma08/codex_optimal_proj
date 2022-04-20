import math


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True



def main():
    n = int(input())
    for i in range(n):
        x = int(input())
        print(is_prime(x))

if __name__ == "__main__":
    main()
