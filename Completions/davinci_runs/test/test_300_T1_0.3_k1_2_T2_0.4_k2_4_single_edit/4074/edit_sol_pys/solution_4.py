
# Solution

import sys

def main():
    t = int(sys.stdin.readline())
    for _ in range(t):
        n, k = map(int, sys.stdin.readline().split())
        print(n // k + (n % k != 0))

if __name__ == '__main__':
    main()
