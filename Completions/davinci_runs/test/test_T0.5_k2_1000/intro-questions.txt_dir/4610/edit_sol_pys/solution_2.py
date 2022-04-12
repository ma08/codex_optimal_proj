

def main():
    N, K = map(int, input().split())
    A = list(map(int, input().split()))
    diff = [0] * (N + 1)
    for i in range(N):
        diff[A[i]] += 1
    diff.sort()
    ans = 0
    for i in range(N - K):
        ans += diff[i]
    print(ans)


if __name__ == '__main__':
    main()
