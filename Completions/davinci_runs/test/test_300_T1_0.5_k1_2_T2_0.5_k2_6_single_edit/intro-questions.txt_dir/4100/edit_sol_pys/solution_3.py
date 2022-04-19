

N, K = [int(i) for i in input().split()]
A = [int(i) for i in input().split()]

# print(A)

sum = 0
for i in range(N):
    if i == 0:
        sum += A[-1] + A[i] + A[i + 1]
    elif i == N - 1:
        sum += A[i - 1] + A[i] + A[0]
    else:
        sum += A[i - 1] + A[i] + A[i + 1]

print(sum)
