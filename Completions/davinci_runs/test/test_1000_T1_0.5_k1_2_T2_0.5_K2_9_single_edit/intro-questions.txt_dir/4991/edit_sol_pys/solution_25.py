

import sys

def h(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return n + h(n/2)
    else:
        return n + h((3*n) + 1)

def main():
    num = int(sys.stdin.readline())
    print(h(num))

if __name__ == '__main__':
    main()
