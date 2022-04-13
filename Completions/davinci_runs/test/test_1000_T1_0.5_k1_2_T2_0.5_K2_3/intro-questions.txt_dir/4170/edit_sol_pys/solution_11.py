def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    if n == 1:
        print(1)
        exit()
    while n > 0:
        n -= 1
        if n == 0:
            ans += 1
        if h[n] >= h[n-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
