

# -----Main-----
a, b, c = input().split()

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"):
    print("No")
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"):
    print("No")
else:
    print("Yes")
