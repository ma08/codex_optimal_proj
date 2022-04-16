

# get input
l, r = map(int, input().split())

# if l and r are equal
if l == r:
    print("Even {}".format(2*l))
# if l and r are not equal
elif l != r:
    print("Odd {}".format(2*max(l, r)))
# if l and r are both 0
else:
    print("Not a moose")
