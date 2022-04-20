

import sys


def main(pname):
    sys.stdin = open(pname + '.in', 'r')
    sys.stdout = open(pname + '.out', 'w')

    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    cnt = [0 for _ in range(k + 1)]
    for el in arr:
        cnt[el] += 1
    lim = min(k, max(cnt[1:]))
    if lim == 0:
        print('NO')
    else:
        print('YES')
        ans = [0 for _ in range(n)]
        j = 0
        for i in range(n):
            if cnt[arr[i]] > 0 and j < lim:
                ans[i] = j
                cnt[arr[i]] -= 1
                if cnt[arr[i]] == 0:
                    j += 1 
        print(*ans)


if __name__ == "__main__":
    main('color')
