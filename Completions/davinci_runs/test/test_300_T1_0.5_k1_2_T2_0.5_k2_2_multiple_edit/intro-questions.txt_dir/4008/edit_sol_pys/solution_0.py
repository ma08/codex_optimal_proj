def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {}
    for i in range(n):
        if a[i] in d:
            d[a[i]] += 1
        else:
            d[a[i]] = 1
    if len(d) > k:
        print("NO")
        return
    ans = [0] * (n + 1)
    cnt = 1
    for i in range(1, n + 1):
        if a[i] in d:
            ans[i] = str(cnt)
            d[a[i]] -= 1
            if d[a[i]] == 0:
                cnt += 1
            if cnt > k:
                print("NO")
                return
    print("YES")
    print(' '.join(ans[1:]))


if __name__ == '__main__':
    main()
