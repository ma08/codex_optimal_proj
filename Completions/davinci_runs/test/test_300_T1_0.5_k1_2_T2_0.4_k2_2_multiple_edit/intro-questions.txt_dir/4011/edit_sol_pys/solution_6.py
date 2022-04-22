import sys
import math



def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n % i == 0:
                return False
        return True


def main():
    n = int(input())
    for i in range(n):
        num = int(input())
        if is_prime(num):
            print('Prime')
        else:
            print('Not prime')


if __name__ == '__main__':
    main()
