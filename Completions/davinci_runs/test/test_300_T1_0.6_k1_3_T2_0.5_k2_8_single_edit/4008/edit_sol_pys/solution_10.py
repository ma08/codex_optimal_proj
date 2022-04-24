

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r', encoding='utf8')
    sys.stdout = open(pname + '.out', 'w', encoding='utf8')

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0 for _ in range(n + 1)]
    for el in arr:
        cnt[el] += 1
    lim = min(k, max(cnt) - 1)
    if lim == 0:
        print('NO')
    else:
        print('YES')
        ans = [0 for _ in range(n)]
        j = 0
        for i in range(n):
            j += 1
            if cnt[arr[i]] > 0:
                ans[i] = j
                cnt[arr[i]] -= 1
                if cnt[arr[i]] == 0:
                    j = 0
        print(*ans)


if __name__ == "__main__":
    main('color')
