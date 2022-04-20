

import sys, math

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    b = list(map(int, sys.stdin.readline().split()))
    c = list(map(int, sys.stdin.readline().split()))
    a.sort()
    b.sort()
    c.sort()
    ans = 0
    for i in range(n):
        ans += b[i] * (a.index(b[i]) + c.index(b[i]) + 2)
    print(ans)

if __name__ == "__main__":
    main()
