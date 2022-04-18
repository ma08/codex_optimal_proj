

# get input and convert to int
n = int(input())

for i in range(n):
    # get input and convert to int
    l, r = map(int, input().split())
    # if l and r are equal, print even
    if l == r:
        print("Even", 2*l)
    # if l and r are not equal
    elif l != r:
        print("Odd", 2*max(l, r))
    # if l and r are both 0
    else:
        print("Not a moose")
