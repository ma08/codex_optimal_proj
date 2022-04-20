N, K = map(int, input().split())
A = list(map(int, input().split()))

sumA = sum(A) - A[K-1]

if sumA / 2 >= N:
    print(0)
    exit()

print(int(N - (sumA / 2)))
