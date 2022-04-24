
def main():
    n = int(input())
    a = list(map(int, input().split()))
    lmin, rmax = a[0], a[-1]
    ans = 0
    for i in range(1, n):
        ans = max(ans, max(a[i] - lmin, rmax - a[i]), a[i] - lmin + rmax - a[i])
        lmin = min(lmin, a[i])
        rmax = max(rmax, a[i])
    print(ans)

if __name__ == '__main__':
    main()
