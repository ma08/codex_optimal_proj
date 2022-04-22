

# -----Answer-----
x, y = map(int, input().split()) #x,y is input

if y % 2 == 0: # y is even
    if (x * 2 + 4) / 2 == y:
        print("Yes")
    else:
        print("No")
else:
    print("No") # y is odd

# -----Other Answer-----
x, y = map(int, input().split()) #x,y is input

if x * 2 <= y <= x * 4: # x*2 <= y <= x*4
    if y % 2 == 0:
        print("Yes")
    else:
        print("No")
else:
    print("No")
