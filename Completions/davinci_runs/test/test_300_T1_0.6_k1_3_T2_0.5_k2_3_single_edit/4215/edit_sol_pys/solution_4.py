
import sys
input = sys.stdin.readline
 
N, M = map(int, input().split())
A = list(map(int, input().split()))
 
A.sort()
 
for i in range(M):
    if A[i] < 0:
        A[i] = -A[i]
    else:
        break
print(sum(A))
