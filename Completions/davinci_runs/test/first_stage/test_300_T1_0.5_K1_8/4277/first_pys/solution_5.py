

import sys

def main():
    n, a, b = [int(i) for i in sys.stdin.readline().split()]
    if n * a <= b:
        print(n * a)
    else:
        print(b)

if __name__ == '__main__':
    main()