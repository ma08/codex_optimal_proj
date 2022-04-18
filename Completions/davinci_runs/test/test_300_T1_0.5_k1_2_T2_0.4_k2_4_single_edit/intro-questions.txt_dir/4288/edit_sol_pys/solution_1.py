
# Get user input
a, b, c = map(int, input().split()) # map(int, input().split()) splits the input and casts it to an integer

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
