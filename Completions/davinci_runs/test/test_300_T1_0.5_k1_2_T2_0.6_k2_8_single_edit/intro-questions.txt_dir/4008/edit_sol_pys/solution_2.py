
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
    ans = [0] * n
    cnt = 1
    for i in range(n):
        if a[i] in d:
            ans[i] = cnt
            d[a[i]] -= 1
            if d[a[i]] == 0:
                cnt += 1
            if cnt > k:
                print("NO")
                return
    print("YES")
    print(' '.join(map(str, ans)))


if __name__ == '__main__':
    main()
