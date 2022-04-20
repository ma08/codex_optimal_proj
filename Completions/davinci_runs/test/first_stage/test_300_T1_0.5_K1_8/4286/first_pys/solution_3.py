

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for i in range(m):
        x, y, w = map(int, input().split())
        offers.append((x, y, w))
    offers.sort(key=lambda x: x[2])
    res = 0
    for i in range(n):
        res += a[i]
    for i in range(m):
        x, y, w = offers[i]
        if a[x - 1] + a[y - 1] > w:
            res -= a[x - 1] + a[y - 1] - w
            a[x - 1] = min(a[x - 1], w - a[y - 1])
            a[y - 1] = min(a[y - 1], w - a[x - 1])
    print(res)

if __name__ == "__main__":
    main()