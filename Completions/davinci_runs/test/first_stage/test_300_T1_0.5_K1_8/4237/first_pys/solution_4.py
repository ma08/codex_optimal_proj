

import sys

def main():
    # Input
    A, B, C, D = map(int, sys.stdin.readline().split())

    # Calculate
    count = B - A + 1
    count -= B // C - (A - 1) // C
    count -= B // D - (A - 1) // D
    count += B // (C * D) - (A - 1) // (C * D)

    # Output
    print(count)

if __name__ == '__main__':
    main()