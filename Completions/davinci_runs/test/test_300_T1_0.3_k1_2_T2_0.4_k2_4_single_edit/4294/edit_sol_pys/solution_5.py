

# Read input and split it
x, a = input().split()

# Convert the strings to integers
x = int(x)
a = int(a)

# Print 0 if x is less than a, else print 10
if x <= a:
    print(0)
else:
    print(10)
