
# Get user input and convert to list
a, b, c = (int(i) for i in input().split())

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and a != c):
    print('Yes')
else:
    print('No')
