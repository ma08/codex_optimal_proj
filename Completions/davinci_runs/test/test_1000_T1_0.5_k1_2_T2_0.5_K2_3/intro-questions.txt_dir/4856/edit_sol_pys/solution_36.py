
def rev(n):
    return int(str(n)[::-1])

A, B = input().split()
A = int(A)
B = int(B)

if rev(A) > rev(B):
    print(rev(A))
else:
    print(rev(B))
