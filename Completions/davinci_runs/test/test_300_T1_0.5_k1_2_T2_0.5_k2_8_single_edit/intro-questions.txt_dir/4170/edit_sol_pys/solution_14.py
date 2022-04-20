def main():
    N = int(input())
    h = list(map(int, input().split(' ')))
    ans = 0
    while N > 0:
        N -= 1
        if N == 0:
            ans += 1
            break
        if h[N] >= h[N-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
