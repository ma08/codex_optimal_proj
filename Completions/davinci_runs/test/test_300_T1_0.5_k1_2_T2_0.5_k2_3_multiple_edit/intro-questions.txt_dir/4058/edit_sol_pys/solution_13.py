
import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    a.sort()
    ans = 0
    i = 0
    for i in range(n):
        while i < n and a[i] <= k:
            k -= a[i]
            i += 1
        if i == n:
            break
        ans += 1
        k = 2 * k
    print(ans)

if __name__ == '__main__':
    main()
