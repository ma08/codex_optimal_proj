

def main():
    A, B, C, K = map(int, input().split())
    ans = 0
    if A < K:
        ans += A
        K -= A
        if B < K:
            K -= B
            ans -= K
    else:
        ans += K
    print(ans)

if __name__ == '__main__':
    main()