

#-----main-----

a, b = [int(i) for i in input().split()]

if a == b and a != 0:
    print("Even " + str(a + b))
elif a != b:
    print("Odd " + str(max(a, b) * 2))
else:
    print("Not a moose")
