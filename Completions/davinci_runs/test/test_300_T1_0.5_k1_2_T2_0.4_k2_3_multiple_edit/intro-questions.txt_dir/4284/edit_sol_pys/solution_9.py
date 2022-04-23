

import sys

def main():
    q = int(sys.stdin.readline())
    for _ in range(q):
        n, k, x, y = map(int, sys.stdin.readline().split())
        if x < y:
            print(-1)
            continue
        if k <= x:
            print(0)
            continue
        if k > x + y:
            print(n)
            continue
        ans = 0
        while k > x + y:
            k -= x
            ans += 1
        if k <= x:
            print(ans)
        else:
            print(ans + 1)

if __name__ == "__main__":
    main()
