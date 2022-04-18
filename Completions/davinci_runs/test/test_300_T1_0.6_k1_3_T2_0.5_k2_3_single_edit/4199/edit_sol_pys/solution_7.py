import sys

N = int(input())
A = list(map(int, input().split()))

max_a = max(A)

A.remove(max_a)

print(max(A))
