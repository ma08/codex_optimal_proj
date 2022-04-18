

def main():
    n = int(input())
    # print(a)
    a = list(map(int, input().split()))
    # print('lmin', lmin)
    lmin = a[0]
    # print('rmax', rmax)
    rmax = a[-1]
    # print('ans', ans)
    ans = 0
        # print('a[i]', a[i])
    for i in range(1, n):
        # print('ans', ans)
        ans = max(ans, max(a[i] - lmin, rmax - a[i]))
        # print('lmin', lmin)
        lmin = min(lmin, a[i])
        # print('rmax', rmax)
        rmax = max(rmax, a[i])
    print(ans)

if __name__ == '__main__':
    main()
