

def main():
    N, K = map(int, input().split())
    h = list(map(int, input().split()))
    h.sort()
    ans = 0
    for i in range(N - K):
        ans += h[i]
    print(ans)

if __name__ == '__main__':
    main()
