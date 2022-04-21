

# Get user input
a, b, c = map(int, input().split()) # a = 1, b = 2, c = 3

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a): # 1 == 2 and 2 != 3
    print('Yes')
else:
    print('No')
