
#-----Main-----#
a, b = input().split()
a = int(a)
b = int(b)
if a == 1:
    if b == 2:
        print("3")
    elif b == 3:
        print("2")
elif a == 2:
    if b == 1:
        print("3")
    elif b == 3:
        print("1")
elif a == 3:
    if b == 1:
        print("2")
    elif b == 2:
        print("1")
elif a == b:
    print(a)
