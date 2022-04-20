

def main():
    n = int(input())
    a = list(map(int, input().split()))
    lmin = [0] * n
    rmax = [0] * n
    lmin[0] = a[0]
    rmax[-1] = a[-1]
    ans = 0
    for i in range(1, n - 1):
        lmin[i] = min(lmin[i - 1], a[i])
        rmax[n - i - 1] = max(rmax[n - i], a[n - i - 1])
    for i in range(n - 1):
        ans = max(ans, max(a[i] - lmin[i], rmax[i] - a[i]))
    print(ans)

if __name__ == '__main__':
    main()
