N = int(input())
S = input()


ans = 0

count = 0

for i in range(N - 1):
    for j in range(i + 1, N):
        count += A[i] * A[j]

print(count % (10 ** 9 + 7))
