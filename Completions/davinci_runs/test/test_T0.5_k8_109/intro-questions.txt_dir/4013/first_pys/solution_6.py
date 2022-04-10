

import sys

def main():
    n = int(input())
    a = [int(x) for x in input().split()]
    a.sort()
    if n == 2:
        print(0)
    else:
        print(min(a[n-2] - a[0], a[n-1] - a[1]))

if __name__ == "__main__":
    main()