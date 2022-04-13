
def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    ans = 0
    for i in range(N - K + 1):
        if A[i] < A[i + K - 1]:
            ans += 1
    print(ans)

if __name__ == '__main__':
    main()
