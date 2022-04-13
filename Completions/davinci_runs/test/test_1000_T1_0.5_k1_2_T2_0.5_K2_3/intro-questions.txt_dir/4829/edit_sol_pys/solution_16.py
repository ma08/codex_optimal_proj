

l, r = map(int, input().split())

if l == r:
    print("Even",(l+r)) 
elif l > r:
    print("Odd",(l*2))
elif r > l:
    print("Odd",(r*2))
else:
    print("Not a moose")
