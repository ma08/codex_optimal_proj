

def main():
    N, K, X = map(int, input().split())
    A = list(map(int, input().split()))[:N]
    if X < K:
        print(-1)  # NONE
    else:
        ans = sum(A)
        for i in range(K):
            ans = max(ans, sum(A[:i]) + sum(A[N-K+i:]))
        print(ans)
    return

if __name__ == '__main__':
    main()
