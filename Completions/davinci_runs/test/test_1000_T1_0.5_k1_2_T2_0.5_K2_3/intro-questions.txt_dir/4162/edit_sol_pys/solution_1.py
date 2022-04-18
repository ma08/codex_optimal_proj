from math import gcd

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    max_f = -1
    for i in range(N):
        for j in range(i + 1, N):
            max_f = max(A[i] + A[j] - gcd(A[i], A[j]), max_f)
    print(max_f)
