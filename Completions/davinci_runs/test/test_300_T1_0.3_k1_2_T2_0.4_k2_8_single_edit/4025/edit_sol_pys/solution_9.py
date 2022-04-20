

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(a, b, c) * 7 + min(a, b) * 2 + min(a, c) * 2 + min(b, c) * 2 - min(a, b, c) - min(a, b) - min(a, c) - min(b, c))

if __name__ == '__main__':
    main()
