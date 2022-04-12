

# Get user input and convert to integer
a = int(input())
b = int(input())
c = int(input())

# Determine if poor or not and print result
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
