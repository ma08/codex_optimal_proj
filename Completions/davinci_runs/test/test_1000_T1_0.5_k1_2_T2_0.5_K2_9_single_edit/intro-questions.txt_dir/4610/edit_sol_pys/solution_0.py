
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    cnt = [0] * N
    for i in range(N):
        if A[i] != i+1:
            cnt[A[i]-1] += 1
    cnt.sort()
    ans = 0
    for i in range(N-K):
        ans += cnt[i]
    print(ans)


if __name__ == '__main__':
    main()
