

import sys

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    m = max(a)
    ans = 0
    for i in range(30, -1, -1):
        if m >> i == 0:
            break
        cnt = [0] * (n + 1)
        for j in range(n):
            if a[j] >> i & 1:
                cnt[j + 1] = 1
        for j in range(1, n + 1):
            cnt[j] += cnt[j - 1]
        cnt = [cnt[i + k - 1] - cnt[i] for i in range(n - k + 1)]
        if sum(cnt) >= k:
            ans += 1
            for j in range(n):
                if a[j] >> i & 1:
                    a[j] -= 1 << i
    print(ans)


if __name__ == "__main__":
    main()