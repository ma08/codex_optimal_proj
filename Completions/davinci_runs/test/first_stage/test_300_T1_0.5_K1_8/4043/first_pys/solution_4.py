

import sys

def main():
    n, d, k = map(int, sys.stdin.readline().split())
    if d > (n - 1):
        print("NO")
    else:
        print("YES")
        for i in range(1, n):
            print(i + 1, i)

if __name__ == '__main__':
    main()