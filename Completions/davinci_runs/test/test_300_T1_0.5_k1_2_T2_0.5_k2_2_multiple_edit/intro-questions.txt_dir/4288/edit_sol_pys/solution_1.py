
# Get user input
a, b, c = map(int, input().split())  # input() is a function

# Determine if poor or not
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):  # if statement
    print('Yes')
else:
    print('No')  # print() is a function
