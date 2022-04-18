
import sys


def main():
    n = int(sys.stdin.readline())
    while n != 0:
        if n == 180:
            print('triple 20')
            print('triple 20')
            print('triple 20')
            return
        if n % 3 == 0:
            print('triple ' + str(n // 3))
            return
        if n % 2 == 0:
            print('double ' + str(n // 2))
            return
        print('single ' + str(n))
        n = int(sys.stdin.readline())


if __name__ == "__main__":
    main()
