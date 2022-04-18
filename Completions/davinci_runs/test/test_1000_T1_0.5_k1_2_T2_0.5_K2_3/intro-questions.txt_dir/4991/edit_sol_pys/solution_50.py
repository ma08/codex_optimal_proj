

import sys

def f(n):
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        print(n)
    return int(n)

def main():
    num = int(sys.stdin.readline().strip())
    f(num)

if __name__ == '__main__':
    main()
