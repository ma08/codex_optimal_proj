
N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

count = 0
for i in range(N):
    if A[i] > B[i]:
        count += 1

print(count)
