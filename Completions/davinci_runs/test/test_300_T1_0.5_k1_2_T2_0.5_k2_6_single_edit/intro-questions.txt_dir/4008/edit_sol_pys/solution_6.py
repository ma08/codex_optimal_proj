
def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = {i: 0 for i in range(1, k + 1)}
    for i in a:
        d[i] += 1
    if max(d.values()) > n // k + 1:
        print('NO')
    else:
        print('YES')
        ans = []
        for i in range(1, k + 1):
            ans += [i] * d[i]
        while len(ans) < n:
            ans.append(1)
        print(*ans)


if __name__ == '__main__':
    main()
