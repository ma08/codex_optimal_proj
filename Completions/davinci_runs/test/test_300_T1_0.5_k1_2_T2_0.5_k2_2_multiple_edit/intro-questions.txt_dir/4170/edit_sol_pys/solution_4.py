def main():
    n = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(n-1):
        if h[i] >= h[i+1]:
            ans += h[i] - h[i+1] + 1
            h[i+1] = h[i] + 1
    print(ans)

if __name__ == '__main__':
    main()
