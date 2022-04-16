

#-----main-----
a, b, c = input().split()

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East") or (b == "North" and c == "South") or (b == "South" and c == "North") or (b == "East" and c == "West") or (b == "West" and c == "East"):
    print("No")
else:
    print("Yes")
