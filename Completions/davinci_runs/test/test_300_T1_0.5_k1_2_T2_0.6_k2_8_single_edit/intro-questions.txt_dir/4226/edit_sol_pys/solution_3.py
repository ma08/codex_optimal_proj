

# -----Other Answer-----
x, y = map(int, input().split()) # input x, y

if x * 2 <= y <= x * 4: # if x*2 <= y <= x*4
    if y % 2 == 0: # if y is even
        print("Yes")
    else:
        print("No") # if y is odd
else:
    print("No") # if y is not x*2 <= y <= x*4

# -----Answer-----
x, y = map(int, input().split()) # input x, y

if y % 2 == 0: # if y is even
    if (x * 2 + 4) / 2 == y: # if (x*2 + 4)/2 == y
        print("Yes") # Yes
    else:
        print("No") # No
else:
    print("No") # if y is odd
