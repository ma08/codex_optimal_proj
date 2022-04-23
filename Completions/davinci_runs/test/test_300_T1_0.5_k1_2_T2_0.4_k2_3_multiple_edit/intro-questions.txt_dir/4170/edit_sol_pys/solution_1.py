
def main():
    n = int(input())
    h = list(map(int, input().split()))  # list of heights
    ans = 0
    while n > 0:
        n -= 1
        if n == 0:
            ans += 1
            break
        if h[n-1] >= h[n]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
