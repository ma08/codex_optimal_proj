

# Get user input
a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
