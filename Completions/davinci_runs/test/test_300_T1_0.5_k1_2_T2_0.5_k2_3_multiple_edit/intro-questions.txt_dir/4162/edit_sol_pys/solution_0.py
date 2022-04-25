

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    max_ans = 0
    for i in range(N):
        for j in range(i + 1, N):
            max_ans = max(max_ans, A[i] + A[j] - gcd(A[i], A[j]))
    print(max_ans)
