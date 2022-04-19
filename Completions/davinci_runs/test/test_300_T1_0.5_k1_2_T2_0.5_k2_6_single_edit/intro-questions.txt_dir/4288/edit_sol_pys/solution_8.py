
# Get user input
a, b, c = map(int, input().split())

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a) or (a == b and b == c):
    print('Yes')
else:
    print('No')
