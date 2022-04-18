

import sys
import math

def main():
    n = int(sys.stdin.readline())
    print(1 - math.factorial(n) / (math.factorial(n-1) * n))

if __name__ == '__main__':
    main()