

import sys

def main():
    a, b, c = map(int, sys.stdin.readline().split())
    print(min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c) + min(a, b, c))

if __name__ == '__main__':
    main()
