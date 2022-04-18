

def reverse(n):
    return int(str(n)[::-1])

A, B = input().split()
A = int(A)
B = int(B)

print(max(reverse(A), reverse(B)))
