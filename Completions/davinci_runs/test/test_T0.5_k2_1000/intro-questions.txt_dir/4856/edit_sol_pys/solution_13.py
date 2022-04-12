

def reverse(n):
    return int(str(n)[::-1])

A, B = input().split()
A = int(A)
B = int(B)

if reverse(A) > reverse(B):
    print(reverse(A))
else:
    print(reverse(B))
