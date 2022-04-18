

# Get user input and convert to integers
a, b, c = map(int, input('Enter three integers: ').split())

# Determine if poor, print result
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
