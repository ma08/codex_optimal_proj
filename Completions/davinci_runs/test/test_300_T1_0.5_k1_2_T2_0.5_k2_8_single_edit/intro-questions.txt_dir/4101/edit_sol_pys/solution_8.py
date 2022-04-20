def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    ans = 0
    for i in range(n):
        if a[i] > k:
            break
        else:
            ans += 1
            k -= a[i]
    print(ans)



if __name__ == '__main__':
    main()
