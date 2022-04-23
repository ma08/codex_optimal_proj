from math import gcd

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    max_f = A[0] + A[1] - gcd(A[0], A[1])
    for i in range(N):
        for j in range(i + 1, N):
            max_f = max(max_f, A[i] + A[j] - gcd(A[i], A[j]))
    print(max_f)
