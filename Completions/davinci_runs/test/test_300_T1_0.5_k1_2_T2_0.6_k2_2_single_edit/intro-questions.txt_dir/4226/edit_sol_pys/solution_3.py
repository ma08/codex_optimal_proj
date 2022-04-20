
# -----Answer-----
X, Y = map(int, input().split())

if Y % 2 == 0:
    if (X * 2 + 4) / 2 == Y:
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----Other Answer-----
X, Y = map(int, input().split())

if X * 2 <= Y <= X * 4:
    if Y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
