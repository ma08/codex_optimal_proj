
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    while n > 0:
        n -= 1
        if n == 0:
            ans += 1
            break
        if a[n-1] >= a[n]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
