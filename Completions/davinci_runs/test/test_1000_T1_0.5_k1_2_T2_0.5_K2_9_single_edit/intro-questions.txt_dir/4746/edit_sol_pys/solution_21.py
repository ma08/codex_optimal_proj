from collections import Counter
import sys

def main():
    input = sys.stdin.readline
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    c = Counter(a)
    a.sort()
    ans = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] + a[j] <= m:
                ans += c[a[i]] * c[a[j]]
            else:
                break
    print(ans)

if __name__ == '__main__':
    main()
