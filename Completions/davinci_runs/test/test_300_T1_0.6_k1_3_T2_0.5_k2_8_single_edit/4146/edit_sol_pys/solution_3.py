
import sys

def main():
    input = sys.stdin.readline
    n, k = map(int, input().split())
    a = list(map(int, input().split()))[:n]

    ans = 0
    for i in range(n - 1):
        for j in range(i + 1, n):
            if a[i] > a[j]:
                ans += 1

    m = 10 ** 5 + 1
    for i in range(10 ** 5 + 1):
        if cnt[i] == 0:
            continue
        if cnt[i] == 2:
            m = min(m, cnt[i])
            continue
        if cnt[i] > 2:
            m = min(m, cnt[i] - 2)

    print(m)

if __name__ == '__main__':
    main()
