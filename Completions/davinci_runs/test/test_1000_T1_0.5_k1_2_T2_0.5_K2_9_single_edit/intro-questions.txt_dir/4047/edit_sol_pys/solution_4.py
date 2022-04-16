

import sys

def main():
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    if n % 2 == 0:
        print(a[n//2] - a[n//2 - 1])
    else:
        print(0)

if __name__ == "__main__":
    main()
