

import sys

def main():
    a, b, c, d, e, f = map(int, sys.stdin.readline().split())
    max_s = (a + b + c) / 2
    max_w = (d + e + f) / 2
    if max_s >= max_w:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
