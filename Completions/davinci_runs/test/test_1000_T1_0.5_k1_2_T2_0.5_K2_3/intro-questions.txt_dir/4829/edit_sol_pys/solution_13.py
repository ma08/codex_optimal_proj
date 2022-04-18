
l, r = [int(i) for i in input().split()]
if l > 0:
    if l == r:
        print("Even ", l*2)
    else:
        print("Odd ", max(l, r)*2)
else:
    print("Not a moose")
