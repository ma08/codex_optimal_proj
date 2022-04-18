
l, r = [int(i) for i in input().split()]
if l == r:
    if l > 0:
        print("Even", l*2)
    else:
        print("Not a moose")
else:
    print("Odd", max(l, r)*2)
