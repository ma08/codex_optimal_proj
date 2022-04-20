

A, B, C = input().split()
A = int(A)
B = int(B)
C = int(C)

if B < A:
    print(0)
elif B >= A * C:
    print(C)
else:
    print(B // A)