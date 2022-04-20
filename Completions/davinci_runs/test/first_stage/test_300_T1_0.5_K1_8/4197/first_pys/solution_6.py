

import sys

N = int(input())
A = list(map(int, input().split()))

# リストを作る
l = [0] * N

for i in range(N):
    l[A[i]-1] = i+1

for i in range(N):
    sys.stdout.write(str(l[i]) + " ")