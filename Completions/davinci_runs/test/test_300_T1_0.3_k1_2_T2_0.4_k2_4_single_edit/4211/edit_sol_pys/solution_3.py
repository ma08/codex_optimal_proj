
N = int(input())
B = list(map(int, input().split()))

A = []
for i in range(N):
    if i == 0:
        A.append(B[i])
    elif i == N-1:
        A.append(B[i-1])
    else:
        A.append(max(B[i-1], B[i]))

print(sum(A))
