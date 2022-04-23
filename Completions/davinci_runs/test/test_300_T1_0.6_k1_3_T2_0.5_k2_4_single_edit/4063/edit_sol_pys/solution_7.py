import sys

X = int(sys.stdin.readline().rstrip())
Y = int(sys.stdin.readline().rstrip())
Z = int(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())

A = list(map(int, sys.stdin.readline().rstrip().split()))
B = list(map(int, sys.stdin.readline().rstrip().split()))
C = list(map(int, sys.stdin.readline().rstrip().split()))

AB = []

for i in range(X):
    for j in range(Y):
        AB.append(A[i] + B[j])

AB.sort(reverse=True)

ABC = []

for i in range(min(K, X * Y)):
    for j in range(Z):
        ABC.append(AB[i] + C[j])

ABC.sort(reverse=True)

for i in range(K):
    print(ABC[i])
