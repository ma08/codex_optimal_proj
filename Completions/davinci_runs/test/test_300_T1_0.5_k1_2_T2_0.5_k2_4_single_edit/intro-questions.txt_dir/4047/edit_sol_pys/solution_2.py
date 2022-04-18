

import sys

def main():
    n = int(input())
    x = list(map(int, input().split()))[:n]
    if len(x) % 2 == 0:
        print(x[len(x)//2] - x[len(x)//2 - 1])
    else:
        print(0)

if __name__ == "__main__":
    main()
