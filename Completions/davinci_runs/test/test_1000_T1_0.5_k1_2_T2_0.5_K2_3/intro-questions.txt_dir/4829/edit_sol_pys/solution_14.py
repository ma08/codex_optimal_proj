

# Get input
l, r = map(int, input().split())

# If l and r are equal
if l == r:
    print("Even", 2*l)
# If l and r are not equal, and at least one of them is not 0
elif l != r and l != 0 and r != 0:
    print("Odd", 2 * max(l, r))
# If l and r are both 0, or if one of them is 0
else:
    print("Not a moose")
