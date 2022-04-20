def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    if n == k:
        print(0)
        return
    a.sort()
    ans = 0
    for i in range(k):
        ans += a[i]
    print(ans)



if __name__ == '__main__':
    main()
