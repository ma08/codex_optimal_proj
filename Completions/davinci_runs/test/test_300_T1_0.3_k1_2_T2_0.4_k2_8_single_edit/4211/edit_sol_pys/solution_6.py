

# My answer
N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
    if i == 0:
        A.append(B[i] - A[i+1] if i+1 < N else B[i])
    elif i == N-1:
        A.append(B[i-1] - A[i-1] if i-1 >= 0 else B[i])
    else:
        A.append(max(B[i-1] - A[i-1], B[i] - A[i+1]))

print(sum(A))
