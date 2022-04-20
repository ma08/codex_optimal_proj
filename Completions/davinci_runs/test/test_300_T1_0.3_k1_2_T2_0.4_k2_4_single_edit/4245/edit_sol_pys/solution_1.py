

import sys

def main():
    line = sys.stdin.readline().rstrip()
    A, B = map(int, line.split())
    print((B - 1) // A + 1)

if __name__ == '__main__':
    main()
