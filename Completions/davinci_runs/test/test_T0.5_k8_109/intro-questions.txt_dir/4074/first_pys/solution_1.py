

import sys

def main():
    t = int(sys.stdin.readline())
    for i in range(t):
        n, k = map(int, sys.stdin.readline().split())
        ans = 0
        for j in range(1, k+1):
            if n % j == 0:
                ans = n // j
                break
        print(ans)


if __name__ == '__main__':
    main()