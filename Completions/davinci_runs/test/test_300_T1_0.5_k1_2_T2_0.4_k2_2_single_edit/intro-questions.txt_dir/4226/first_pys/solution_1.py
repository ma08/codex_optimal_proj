

# -----Answer-----
x, y = map(int, input().split())

if y % 2 == 0:
    if (x * 2 + 4) / 2 == y:
        print("Yes")
    else:
        print("No")
else:
    print("No")

# -----Other Answer-----
x, y = map(int, input().split())

if x * 2 <= y <= x * 4:
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")