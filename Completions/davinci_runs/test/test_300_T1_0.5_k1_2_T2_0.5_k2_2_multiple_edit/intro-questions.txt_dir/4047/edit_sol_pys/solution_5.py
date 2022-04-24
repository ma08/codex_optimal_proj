

import sys

def main():
    n = int(input())
    y = list(map(int, input().split()))
    y.sort()
    print(y[n//2] - y[n//2 - 1])

if __name__ == "__main__":
    main()
