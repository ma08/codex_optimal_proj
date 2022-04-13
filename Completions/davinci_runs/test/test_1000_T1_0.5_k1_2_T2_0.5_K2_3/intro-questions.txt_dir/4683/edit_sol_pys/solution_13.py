
N = int(input())
A = list(map(int, input().split()))

count = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        if A[i] > A[j]:
            count += 1

print(count % (10 ** 9 + 7))
