

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    if n < a:
        print(n)
    else:
        print(a + (n - a) // (a + b) * a - (n - a) % (a + b) if (n - a) % (a + b) < a else a))

if __name__ == '__main__':
    main()
