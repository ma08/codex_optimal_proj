

import sys, math

def main():
    n, m = [int(x) for x in input().split()]
    print(math.ceil(n / m))

if __name__ == "__main__":
    main()
