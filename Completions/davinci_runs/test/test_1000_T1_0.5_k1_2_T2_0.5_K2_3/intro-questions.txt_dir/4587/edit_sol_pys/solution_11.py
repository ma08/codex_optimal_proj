

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()

count = 0

for i in range(N):
    count += bisect.bisect_left(A, B[i]) * (N - bisect.bisect_right(A, C[i]))

print(count)
