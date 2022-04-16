def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))


    a.sort()

    ans = 0
    for i in range(n):
        if x >= a[i]:
            ans += 1
            x -= a[i]

    if x != 0:
        ans -= 1

    print(ans)

if __name__ == '__main__':
    main()
