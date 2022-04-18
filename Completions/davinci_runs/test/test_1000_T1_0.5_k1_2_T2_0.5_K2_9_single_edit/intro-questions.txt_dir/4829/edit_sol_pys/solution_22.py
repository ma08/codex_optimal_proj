

# get input
l, r = map(int, input().split()) # get left and right horns

# if l and r are both 0
if l == 0 and r == 0:
    print("Not a moose")

# if l and r are equal
if l == r:
    print("Even", 2*l)
# if l and r are not equal
elif l != r:
    print("Odd", 2*max(l, r))
