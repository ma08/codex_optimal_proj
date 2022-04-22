

# Get user input
a = int(input())
b = int(input())
c = int(input())

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a)
    print('Yes')
else
    print('No')
