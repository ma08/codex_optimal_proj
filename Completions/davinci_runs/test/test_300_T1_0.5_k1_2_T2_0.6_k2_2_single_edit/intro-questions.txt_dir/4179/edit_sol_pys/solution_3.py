

import sys

def main():
    n = int(sys.stdin.readline())
    a = [int(i) for i in sys.stdin.readline().split()]
    a.sort()
    ans = 0
    for i in range(n):
        ans += a[i]*(n-i)
    print(ans)

if __name__ == "__main__":
    main()
