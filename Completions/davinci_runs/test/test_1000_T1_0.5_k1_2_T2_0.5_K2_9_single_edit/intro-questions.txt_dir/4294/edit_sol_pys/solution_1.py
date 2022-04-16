

# Read two integers from input
x, a = map(int, input().split()) # split() returns a list of strings after breaking the given string by the specified separator.

# If x is less than a, print 0; otherwise, print 10
if x < a:
    print(0)
else:
    print(10)
