

import sys

def main():
    n, t, m = [int(i) for i in sys.stdin.readline().split()]
    print(n * t * m)

if __name__ == "__main__":
    main()