
#-----main-----
a, b, c = input().split()

if (a == "North" and c == "South") or (a == "South" and c == "North") or (a == "East" and c == "West") or (a == "West" and c == "East"):
    print("No")
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"):
    print("No")
else:
    print("Yes")
