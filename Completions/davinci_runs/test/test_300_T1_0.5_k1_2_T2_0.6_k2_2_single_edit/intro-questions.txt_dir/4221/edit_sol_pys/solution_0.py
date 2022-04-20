

from random import randint


def random_number(n, k):
    return randint(n, k)


def main():
    n = int(input())
    k = int(input())
    random_number(n, k)
    print(random_number(n, k))


if __name__ == '__main__':
    main()
