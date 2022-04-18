import math

import sys

def main():
    N = float(sys.stdin.readline().strip())
    print(math.pow(N, 1 / N))

if __name__ == "__main__":
    main()
