

import sys


def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def main():
    num = int(sys.stdin.readline().strip())
    if is_prime(num):
        print(1)
    else:
        print(0)


if __name__ == '__main__':
    main()