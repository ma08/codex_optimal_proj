import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

m = min(A)
c = A.count(m)

if c % 2 == 0:
    print(len(A))
else:
    print(len(A) - 1)
