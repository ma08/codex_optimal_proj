

# Get input
l, r = map(int, input().split())

# If l and r are equal
if l == r:
    print("Even", 2*l)
# If l and r are not equal
elif l != r:
    print("Odd", 2*max(l, r))
# If l and r are both 0 
else:
    print("Not a moose")
