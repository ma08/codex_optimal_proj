
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    c = list(map(int, input().split()))
    a.sort()
    b.sort()
    c.sort()
    d = [0] * n
    e = [0] * m
    for i in range(n):
        if a[i] < b[0]:
            d[i] = 0
        else:
            d[i] = bisect.bisect_left(b, a[i])
    for i in range(m):
        if b[i] < c[0]:
            e[i] = 0
        else:
            e[i] = bisect.bisect_left(c, b[i])
    print(d)
    print(e)
    print(sum(d))
    print(sum(e))
    print(sum(d) * sum(e))


if __name__ == '__main__':
    main()
