

import sys
N = int(input())
A = list(map(int, input().split()))
if A.count(1)>1 or A.count(N)>1:
    print(0)
else:
    print(1)
