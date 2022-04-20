

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    mod = 10 ** 9 + 7
    ans = 0
    for i in range(K):
        ans += A[i] * (N - i)
    tmp = ans
    for i in range(K, N):
        tmp -= A[i - K]
        tmp += A[i]
        ans += tmp
        ans %= mod
    print(ans)

if __name__ == '__main__':
    main()
