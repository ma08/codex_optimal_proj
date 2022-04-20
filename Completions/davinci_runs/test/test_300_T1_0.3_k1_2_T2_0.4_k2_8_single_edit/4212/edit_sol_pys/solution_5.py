

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    for i in range(n):
        if a[i] == 0:
            print(0)
            return
    ans = 1
    for i in range(n):
        ans *= a[i]
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':
    main()
