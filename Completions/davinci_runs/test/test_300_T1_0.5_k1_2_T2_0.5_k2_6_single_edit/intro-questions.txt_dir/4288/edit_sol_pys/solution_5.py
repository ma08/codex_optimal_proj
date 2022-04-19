
# Get user input
a, b, c = map(int, input().split())

# Determine if unique
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
