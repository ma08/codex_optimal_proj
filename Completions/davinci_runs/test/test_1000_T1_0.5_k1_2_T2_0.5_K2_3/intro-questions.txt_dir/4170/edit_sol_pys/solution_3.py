
def main():
    n = int(input())
    # h = list(map(int, input().split()))
    h = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 2, 1]
    ans = 0
    while n > 0:
        n -= 1
        if n == 0:
            ans += 1
            break
        if h[n] >= h[n-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
