
def main():
    n = int(input())
    h = list(map(int, input().split()))[::-1]
    ans = 0
    for i in range(1, n):
        if h[i] > h[i-1]:
            ans += 1
            continue
        elif h[i] == h[i-1]:
            continue
        elif h[i] < h[i-1]:
            ans += h[i-1] - h[i] + 1
            h[i] = h[i-1] + 1
    print(ans)

if __name__ == '__main__':
    main()
