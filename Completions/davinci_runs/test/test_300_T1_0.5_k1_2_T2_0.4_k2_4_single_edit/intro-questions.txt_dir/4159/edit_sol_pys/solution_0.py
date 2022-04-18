

A,B,C = map(int, input().split())

if C <= A:
    A -= C
else:
    C -= A
    A = 0
    if C <= B:
        B -= C
    else:
        B = 0

print(A,B)
