

from bisect import bisect_left, bisect_right

A.sort()
B.sort()
C.sort()

count = 0

for b in B:
    count += bisect_left(A, b) * (N - bisect_right(C, b))

print(count)
