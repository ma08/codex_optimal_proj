

#-----main-----
a, b, c = input().split()

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"):
    print("No")
elif (a == "North" and c == "South") or (a == "South" and c == "North") or (a == "East" and c == "West") or (a == "West" and c == "East"):
    print("No")
else:
    print("Yes")
