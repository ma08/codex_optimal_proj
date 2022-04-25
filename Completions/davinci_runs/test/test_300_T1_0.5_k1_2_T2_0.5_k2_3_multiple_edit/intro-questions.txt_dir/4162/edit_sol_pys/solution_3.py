import fractions

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    max_f = 0
    for i in range(N):
        for j in range(i + 1, N):
            max_f = max(max_f, A[i] + A[j] - fractions.gcd(A[i], A[j]))
    print(max_f)
