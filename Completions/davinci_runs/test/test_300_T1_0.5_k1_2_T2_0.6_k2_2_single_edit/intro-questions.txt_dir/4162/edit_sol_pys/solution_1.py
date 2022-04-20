from collections import defaultdict


def main():
    n, p = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    cnt = defaultdict(int)
    for x in a:
        cnt[x] += 1

    for x in b:
        cnt[x] -= 1

    ans = 0
    for x in a:
        if not cnt[x]:
            continue
        if x * p > b[-1]:
            break
        l, r = 0, len(b)
        while l < r:
            m = (l + r) // 2
            if x * p > b[m]:
                l = m + 1
            else:
                r = m
        ans += len(b) - l

    print(ans)

if __name__ == '__main__':
    main()
