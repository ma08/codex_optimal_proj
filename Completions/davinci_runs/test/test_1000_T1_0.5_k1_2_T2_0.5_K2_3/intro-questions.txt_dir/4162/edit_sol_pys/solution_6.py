
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    max_f = 0
    for i in range(N):
        for j in range(i + 1, N):
            max_f = max(max_f, A[i] + A[j] - gcd(A[i], A[j]))
    print(max_f)
