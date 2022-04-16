

a, b, c, d = input().split()

if (a == "South" and b == "West" and c == "East" and d == "North") or (a == "North" and b == "East" and c == "West" and d == "South") or (a == "West" and b == "North" and c == "South" and d == "East") or (a == "East" and b == "South" and c == "North" and d == "West"):
    print("Yes")
else:
    print("No")
