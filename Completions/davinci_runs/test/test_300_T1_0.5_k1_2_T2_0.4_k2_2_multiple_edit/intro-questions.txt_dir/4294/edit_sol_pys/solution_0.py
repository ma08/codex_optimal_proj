

# Read two integers from input and store them in variables named x and a.
x, a = map(int, input().split()) # map(int, input().split()) returns a list of integers

# If x is less than a, print 0; otherwise, print 10.
if x < a:
    print(0)
else:
    print(10)
