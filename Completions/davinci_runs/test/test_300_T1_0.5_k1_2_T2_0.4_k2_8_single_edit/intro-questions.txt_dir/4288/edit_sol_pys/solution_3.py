

# Get user input
a, b, c = map(int, input().split()) # a is first number, b is second number, c is third number

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a): # if a is equal to b and b is not equal to c, or a is equal to c and c is not equal to b, or b is equal to c and c is not equal to a
    print('Yes')
else: # if a is not equal to b and b is not equal to c, or a is not equal to c and c is not equal to b, or b is not equal to c and c is not equal to a
    print('No')
