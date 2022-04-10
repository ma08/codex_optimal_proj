

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))

    a.sort()
    s = 0
    for k in range(n):
        if s + a[k] - k >= m:
            print(k)
            return
        s += a[k]

    if s >= m:
        print(n)
        return
    else:
        print(-1)
        return


if __name__ == '__main__':
    main()
