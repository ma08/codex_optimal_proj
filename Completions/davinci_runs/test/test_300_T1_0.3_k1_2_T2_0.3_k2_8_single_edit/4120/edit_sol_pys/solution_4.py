

import sys

def main():
    n, m, k = [int(x) for x in sys.stdin.readline().split()]
    roads = [int(x) for x in sys.stdin.readline().split()]
    print(n, m, k)
    print(roads)

if __name__ == "__main__":
    main()
