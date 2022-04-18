
# get input
l, r = map(int, input().split())

# if l and r are equal
if l == r:
    print("Even", 2*l)
# if l and r are not equal
else:
    print("Odd", 2*max(l, r))
