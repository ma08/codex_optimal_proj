

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    if n % a == 0:
        print(n // a, 0)
    elif n % b == 0:
        print(0, n // b)
    elif n % b == a % b:
        print(n // a, (n % a) // b)
    else:
        print("Impossible")

if __name__ == '__main__':
    main()
