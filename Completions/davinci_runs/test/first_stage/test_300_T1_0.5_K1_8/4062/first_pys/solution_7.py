

import sys

def main():
    a, b, c, d = map(int, sys.stdin.readline().split())
    if a > b:
        a, b = b, a
    if c > d:
        c, d = d, c
    print(max(b*d, b*c, a*d, a*c))

if __name__ == '__main__':
    main()