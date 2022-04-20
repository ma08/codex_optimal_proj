
import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))

for i in range(N):
    a = A[i]
    if a % 2 == 0:
        if a % 3 != 0 and a % 5 != 0:
            print("DENIED")
            exit()

print("APPROVED")
