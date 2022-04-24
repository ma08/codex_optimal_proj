
A, B, C, D = map(int, input().split())

if C <= B:
    print(0)
else:
    print(min(A, D) - max(B, C))
