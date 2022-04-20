

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(a, b, c) * 7 + min(a, b, c) * 2 + min(a, c, b) * 2 + min(b, c, a) * 2)

if __name__ == '__main__':
    main()
