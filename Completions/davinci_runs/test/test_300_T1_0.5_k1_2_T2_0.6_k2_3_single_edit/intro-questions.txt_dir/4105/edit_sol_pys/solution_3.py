

n, k = [int(x) for x in input().split()]

if n == 2:
    print("YES")
    print("1 2")
elif n == 3:
    print("YES")
    print("1 2")
    print("2 3")
    print("3 1")
    print("2 1")
else:
    if k == 5:
        print("YES")
        print("1 2")
        print("2 3")
        print("3 4")
        print("4 5")
        print("5 1")
    else:
        print("NO")
