
def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    a.sort()
    b.sort()

    print(a)
    print(b)

    ans = 0
    for i in range(m):
        if a[i] < b[i]:
            ans += 1

    print(ans)


if __name__ == '__main__':
    main()
