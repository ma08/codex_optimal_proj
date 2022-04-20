

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    s = sum(a)
    cur = 0
    ans = 0
    for i in range(n):
        cur += a[i]
        if cur == (s - cur + a[i]):
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()