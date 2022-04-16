

# Get user input from command line
a, b, c = map(int, sys.argv[1:])

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
