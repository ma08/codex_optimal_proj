
import collections
import sys

def main():
    n, m = map(int, input().split())
    d = collections.defaultdict(list)
    for i in range(n):
        a, b = map(int, input().split())
        d[a].append(b)
    for a in d:
        d[a].sort()
    for _ in range(m):
        a, b = map(int, input().split())
        if not d[a]:
            print(-1)
            continue
        if b > d[a][-1]:
            print(-1)
            continue
        l = 0
        r = len(d[a]) - 1
        while l <= r:
            mid = (l + r) // 2
            if d[a][mid] == b:
                print(mid + 1)
                break
            elif d[a][mid] > b:
                r = mid - 1
            else:
                l = mid + 1

if __name__ == '__main__':
    main()
