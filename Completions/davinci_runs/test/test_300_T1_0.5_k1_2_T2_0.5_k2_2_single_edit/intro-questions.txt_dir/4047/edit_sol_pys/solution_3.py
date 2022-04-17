

import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))
    x = sorted(x)
    print(x[n//2] - x[n//2 - 1])

if __name__ == "__main__":
    main()
