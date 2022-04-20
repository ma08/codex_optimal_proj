

import sys, math

def main():
    n, k = [int(x) for x in sys.stdin.readline().strip().split()]
    print(math.ceil((n - 1) / (k - 1)))

if __name__ == "__main__":
    main()
