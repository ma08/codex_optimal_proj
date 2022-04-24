import math

N, M = map(int, input().split())
A = list(map(int, input().split()))

if max(A) >= math.ceil(sum(A) / (4 * M)):
    print('Yes')
else:
    print('No')
