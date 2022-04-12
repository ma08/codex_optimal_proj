

a, b, c = input().split() 

if (a == "South" and b == "West" and c == "East") or (a == "North" and b == "East" and c == "West") or (a == "West" and b == "North" and c == "South") or (a == "East" and b == "South" and c == "North") or (a == "South" and b == "East" and c == "West") or (a == "North" and b == "West" and c == "East") or (a == "West" and b == "South" and c == "North") or (a == "East" and b == "North" and c == "South"):
    print("Yes")
else:
    print("No")
