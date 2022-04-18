

l, r = map(int, input().split())

if l == r:
    print("Even {}".format((l+r)))
elif l > r:
    print("Odd {}".format((l*2)))
elif r > l:
    print("Odd {}".format((r*2)))
