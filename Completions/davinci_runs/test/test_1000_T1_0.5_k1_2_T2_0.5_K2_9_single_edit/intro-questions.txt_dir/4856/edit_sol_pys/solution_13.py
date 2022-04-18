

def reverse(n): # Define a function that reverses the digits of a number.
    return int(str(n)[::-1]) # Return the reversed number.

A, B = input().split()
A = int(A)
B = int(B)

if reverse(A) > reverse(B):
    print(reverse(A))
else:
    print(reverse(B))
