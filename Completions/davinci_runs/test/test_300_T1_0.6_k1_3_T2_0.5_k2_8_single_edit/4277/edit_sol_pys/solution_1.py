

import sys
import math

def main():
    A, B, C = [int(x) for x in sys.stdin.readline().rstrip().split()]
    K = int(sys.stdin.readline().rstrip())
    print(A - B if K % 2 == 0 else B - A)

if __name__ == '__main__':
    main()
