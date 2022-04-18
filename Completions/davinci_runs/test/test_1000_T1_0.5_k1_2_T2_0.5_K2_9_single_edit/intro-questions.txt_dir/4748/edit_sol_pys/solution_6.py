

import sys

def main():
    h, n, m = [int(x) for x in sys.stdin.readline().split()]
    if n + m >= h:
        print('Yes')
    elif n + m < h:
        print('No')

if __name__ == '__main__':
    main()
