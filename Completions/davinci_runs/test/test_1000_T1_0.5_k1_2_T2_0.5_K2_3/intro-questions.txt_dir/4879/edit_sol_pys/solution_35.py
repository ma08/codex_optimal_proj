a, b, c = input().split()
if a == "North":
    if b == "West" and c == "East" or b == "East" and c == "West":
        print("Yes")
    else:
        print("No")
elif a == "South":
    if b == "West" and c == "East" or b == "East" and c == "West":
        print("Yes")
    else:
        print("No")
elif a == "East":
    if b == "North" and c == "South" or b == "South" and c == "North":
        print("Yes")
    else:
        print("No")
elif a == "West":
    if b == "North" and c == "South" or b == "South" and c == "North":
        print("Yes")
    else:
        print("No")
