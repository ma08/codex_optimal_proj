

# -----Answer-----
a, op, b = input().split() # split() returns a list of strings after breaking the given string by the specified separator.

if op == '+': # == is used to check if the values of two operands are equal or not.
    print(int(a) + int(b))
elif op == '-':
    print(int(a) - int(b))
