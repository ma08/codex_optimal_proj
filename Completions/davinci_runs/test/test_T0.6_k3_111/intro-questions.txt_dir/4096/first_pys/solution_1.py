

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort(reverse=True)
    if a[0] > m:
        print(-1)
        return

    s = 0
    for k in range(n):
        if s >= m:
            print(k)
            return
        s += a[k] - k

    if s >= m:
        print(n)
        return
    else:
        print(-1)
        return


if __name__ == '__main__':
    main()