# Get user input
n = int(input())
l=list(map(int,input().split()))


# If a list is empty, print 0
if len(l) == 0:
    print(0)

# Determine if poor
if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
    print('Yes')
else:
    print('No')
