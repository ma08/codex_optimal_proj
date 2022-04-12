

def reverse_int(n):
    return int(str(n)[::-1])

A, B = input().split()
A = int(A)
B = int(B)

if reverse_int(A) > reverse_int(B):
    print(reverse_int(A))
else:
    print(reverse_int(B))
