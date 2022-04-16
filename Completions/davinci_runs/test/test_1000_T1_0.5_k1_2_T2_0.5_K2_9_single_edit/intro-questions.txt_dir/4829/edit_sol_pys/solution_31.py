

l, r = map(int, input().split())

if l == r:
    print("Even {0}".format((l+r)))
elif l > r:
    print("Odd {0}".format((l*2)))
elif r > l:
    print("Odd {0}".format((r*2)))
else:
    print("Not a moose")
