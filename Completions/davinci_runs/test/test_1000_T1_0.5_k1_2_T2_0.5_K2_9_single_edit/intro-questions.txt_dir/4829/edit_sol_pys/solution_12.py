

l, r = [int(l) for l in input().split()]
if l == r and l > 0 and r > 0:
    print("Even", l * 2)
elif l != r and l > 0 and r > 0:
    print("Odd", max(l, r) * 2)
else:
    print("Not a moose")
