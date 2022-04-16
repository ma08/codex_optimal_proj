

# get input and assign to variables
l, r = map(int, input().split()) # split string into list of integers and assign to variables

# if l and r are equal, print "Even" and 2*l
if l == r: 
    print("Even", 2*l)
# if l and r are not equal
elif l != r:
    print("Odd", 2*max(l, r))
# if l and r are both 0
else:
    print("Not a moose")
