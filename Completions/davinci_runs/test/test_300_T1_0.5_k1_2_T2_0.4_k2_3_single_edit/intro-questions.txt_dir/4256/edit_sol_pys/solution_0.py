
A, B, C = map(int, input().split())
if C <= B:
    print(C)
else:
    print(B + (C - B) // (A - B) * (A - B))
