

import sys

def main():
    n = int(sys.stdin.readline())
    a = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    ans = 0
    for i in range(1, n):
        ans += a[i - 1] - a[i]
    print(ans)

if __name__ == '__main__':
    main()
