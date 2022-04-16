import math

import sys

def f(n):
    return n*(n+1)//2

def main():
    lines = [line.strip() for line in sys.stdin]    

    for i, line in enumerate(lines, 1):
        n = int(line)
        print(i, f(n-1))

if __name__ == '__main__':
    main()
