

def main():
    N = int(input())
    h = list(map(int, input().split()))
    ans = 0
    for i in range(1, N - 1):
        if h[i - 1] < h[i] and h[i + 1] < h[i]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()