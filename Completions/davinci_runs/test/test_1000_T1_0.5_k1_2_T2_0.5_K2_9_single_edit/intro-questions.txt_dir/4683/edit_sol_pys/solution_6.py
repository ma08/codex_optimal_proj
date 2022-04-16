

N = int(input()) # 長さNの数列
A = list(map(int, input().split())) # A[0]~A[N-1]までの数列

count = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        count += A[i] * A[j]

print(count % (10 ** 9 + 7))
