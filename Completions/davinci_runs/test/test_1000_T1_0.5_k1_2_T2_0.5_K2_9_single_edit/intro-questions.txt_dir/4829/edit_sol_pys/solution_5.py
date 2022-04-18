

# get input
l, r = map(int, input().split())

# if l and r are both 0
if l == 0 and r == 0:
    print("Not a moose")
# if l and r are different
elif l != r: 
    print("Odd", 2*max(l, r))  
# if l and r are the same
else:
    print("Even", 2*l)
