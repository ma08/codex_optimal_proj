

# Get user input
a, b, c = map(int, input().split()) # Get user input

# Determine if poor 
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
