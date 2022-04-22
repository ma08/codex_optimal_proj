

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = dict()
    for i in a:
        if i in d:
            d[i] += 1
    if len(d) < k:
        print("NO")
        return
    ans = [0]*n
    c = 1
    for i in a:
        ans[i] = c
        d[i] -= 1
        if d[i] == 0:
            c += 1
    print("YES")
    print(*ans)


if __name__ == '__main__':
    main()
