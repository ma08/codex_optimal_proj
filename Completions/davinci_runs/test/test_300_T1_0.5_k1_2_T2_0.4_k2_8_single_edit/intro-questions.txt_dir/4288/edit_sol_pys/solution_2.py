

# Get user input
a, b, c, d = map(int, input().split())

# Determine if poor
if (a + b == c + d) or (a + c == b + d) or (a + d == b + c) or (a == b + c + d) or (b == a + c + d) or (c == a + b + d) or (d == a + b + c):
    print('Yes')
else:
    print('No')
