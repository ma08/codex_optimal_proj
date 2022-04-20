

import sys

def main():
    n, a, b = map(int, sys.stdin.readline().split())
    print(n if n < a else a + (n - a) // (a + b) * a - (n - a) % (a + b) if (n - a) % (a + b) < a else a)

if __name__ == '__main__':
    main()
