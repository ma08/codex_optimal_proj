

N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

A.sort()
B.sort()
C.sort()

count = 0

for b in B:
    count += bisect_left(A, b) * (N - bisect_left(C, b))

print(count)
