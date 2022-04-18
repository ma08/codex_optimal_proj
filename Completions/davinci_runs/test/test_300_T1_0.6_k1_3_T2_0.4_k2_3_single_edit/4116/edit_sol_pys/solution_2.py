
import sys

N = int(sys.stdin.readline())

for i in range(2, N):
    if N % i == 0:
        print("No")
        exit()
print("Yes")
