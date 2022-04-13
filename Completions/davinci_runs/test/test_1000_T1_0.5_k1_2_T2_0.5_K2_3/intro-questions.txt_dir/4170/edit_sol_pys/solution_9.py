def main():
    n, k = list(map(int, input().split()))
    h = list(map(int, input().split()))[:n]
    ans = 0
    for i in range(n):
        if i == 0:
            ans += 1
            continue
        if h[i] >= h[i-1]:
            ans += 1
        else:
            break
    print(ans)

if __name__ == '__main__':
    main()
