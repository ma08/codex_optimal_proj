
# -----Answer 1-----
x, y = map(int, input().split()) # input x, y

if y % 2 == 0: # if y is even
    if (x * 2 + 4) / 2 == y: # if x is odd
        print("Yes")
    else: # if x is even
        print("No")
else: # if y is odd
    print("No")

# -----Answer 2-----
x, y = map(int, input().split()) # input x, y

if x * 2 <= y <= x * 4: # if y is in range of 2x and 4x
    if y % 2 == 0: # if y is even
        print("Yes")
    else: # if y is odd
        print("No")
else: # if y is not in range of 2x and 4x
    print("No")
