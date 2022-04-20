
def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    while n > 1:
        n -= 1
        if h[n] >= h[n-1]:
            ans += 1
        else:
            break
    ans += 1
    print(ans)

if __name__ == '__main__':
    main()
