

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

total = 0

for i in range(N):
    total += B[A[i] - 1]
    if i > 0 and A[i] == A[i - 1] + 1:
        total += C[A[i - 1] - 1]

print(total)