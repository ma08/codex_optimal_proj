

a, b, c = input().split()

if (a == "South" and b == "West" and c == "East") or (a == "North" and b == "West" and c == "East") or (a == "West" and b == "North" and c == "East") or (a == "East" and b == "South" and c == "North"):
    print("Yes")
else:
    print("No")
