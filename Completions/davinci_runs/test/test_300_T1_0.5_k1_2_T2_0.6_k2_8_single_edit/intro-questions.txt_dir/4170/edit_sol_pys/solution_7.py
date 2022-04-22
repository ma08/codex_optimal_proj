
def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while n > 0:
        n -= 1
        if n == 0:
            ans += 1
            break
        if h[n] < h[n-1]:
            break
        else:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
