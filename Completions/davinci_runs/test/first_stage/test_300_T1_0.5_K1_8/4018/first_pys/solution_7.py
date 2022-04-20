

import sys

def main():
    n, k = map(int, sys.stdin.readline().split())
    s = sys.stdin.readline().strip()
    if k > n*(n+1)//2:
        print(-1)
        return

    ans = 0
    for i in range(n):
        for j in range(i, n):
            sub = s[i:j+1]
            cnt = len(sub)
            if cnt > k:
                break
            k -= cnt
            ans += n - cnt
        if k == 0:
            break
    print(ans)

if __name__ == '__main__':
    main()