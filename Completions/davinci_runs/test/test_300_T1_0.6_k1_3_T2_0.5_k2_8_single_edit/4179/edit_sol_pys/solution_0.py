

N = int(input())
A = list(map(int, input().split()))

A.sort()

result = A[0]
for i in range(1, N):
    result = (result + A[i]) / 2

print(result)
