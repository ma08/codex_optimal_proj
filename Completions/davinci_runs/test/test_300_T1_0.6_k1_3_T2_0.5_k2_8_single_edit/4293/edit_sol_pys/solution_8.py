

import sys

readline = sys.stdin.readline

def main():
    A, B, C = map(int, readline().split())

    print(min(A+B, B+C, C+A))

if __name__ == '__main__':
    main()
