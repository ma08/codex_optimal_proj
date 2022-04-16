
N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N):
    for j in range(N):
        if i < j:
            count += A[i] * A[j]

print(count % (10 ** 9 + 7))
