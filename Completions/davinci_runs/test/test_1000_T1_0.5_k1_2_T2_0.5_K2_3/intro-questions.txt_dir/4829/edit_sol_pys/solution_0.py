

l, r = map(int, input().split())

if l == r:
    print("Even {}".format(((l+r)//2) * 2))
elif l > r:
    print("Odd {}".format(((l*2)+1)))
elif r > l:
    print("Odd {}".format(((r*2)+1)))
else:
    print("Not a moose")
