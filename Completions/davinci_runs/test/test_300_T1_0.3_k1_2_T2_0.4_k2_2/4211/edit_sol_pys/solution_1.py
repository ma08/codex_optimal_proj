

# My answer
N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
    if i == 0:
        A.append(B[i] - A[i-1])
    elif i == N-1:
        A.append(B[i-1] - A[i-2])
    else:
        A.append(max(B[i-1] - A[i-2], B[i] - A[i-1]))

print(sum(A))
