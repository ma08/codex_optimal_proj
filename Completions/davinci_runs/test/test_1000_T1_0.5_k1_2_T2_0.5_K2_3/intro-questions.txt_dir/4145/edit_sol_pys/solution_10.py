
import math

def main():
    # input
    x = int(input())

    # calculate the minimum prime number
    prime_num = x
    while True:
        if is_prime(prime_num):
            break
        else:
            prime_num += 1

    # output the result
    print(prime_num)

def is_prime(n):
    """
    check if n is prime.
    """
    if n == 1:
        return False
    else:
        for i in range(2, math.floor(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

if __name__ == '__main__':
    main()
