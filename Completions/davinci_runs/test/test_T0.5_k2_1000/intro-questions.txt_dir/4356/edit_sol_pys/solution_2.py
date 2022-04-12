import sys

n, m = map(int, sys.stdin.readline().strip().split())
A = []
for i in range(n):
    A.append(sys.stdin.readline().strip())
B = []
for i in range(m):
    B.append(sys.stdin.readline().strip())

for i in range(n - m + 1):
    for j in range(n - m + 1):
        match = True
        for k in range(m):
            if A[i + k][j:j + m] != B[k]:
                match = False
                break
        if match:
            print("Yes")
            sys.exit()
print("No")
