

a, b, c, d = [int(x) for x in input().split()]

if a > b:
    print("Gunnar")
elif a < b:
    print("Emma")
else:
    if c > d:
        print("Emma")
    elif c < d:
        print("Gunnar")
    else:
        print("Tie")



