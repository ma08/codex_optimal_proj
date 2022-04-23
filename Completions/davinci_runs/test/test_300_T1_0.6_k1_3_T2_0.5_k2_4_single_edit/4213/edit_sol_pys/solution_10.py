
def main():
    n = int(input())
    a = list(map(int, input().split()))
    lmin = a[1]
    rmax = a[n-1]
    ans = 0
    for i in range(2, n-1):
        ans = max(ans, max(a[i] - lmin, rmax - a[i]))
        lmin = min(lmin, a[i])
        rmax = max(rmax, a[i])
    print(ans)

if __name__ == '__main__':
    main()
