

l, r = [int(i) for i in input().split()]
if l == r and l > 0:
    print("Even", l * 2)
elif l != r:
    print("Odd", max(l, r) * 2)
else:
    print("Not a moose") 
