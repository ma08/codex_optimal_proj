
import sys
input = sys.stdin.readline
 
N = int(input())
A = list(map(int, input().split()))
 
B = [0] * N
for i in range(N):
    if i % 2 == 0:
        B[i // 2] = A[i]
    else:
        B[N - i // 2 - 1] = A[i]
 
print(*B)
