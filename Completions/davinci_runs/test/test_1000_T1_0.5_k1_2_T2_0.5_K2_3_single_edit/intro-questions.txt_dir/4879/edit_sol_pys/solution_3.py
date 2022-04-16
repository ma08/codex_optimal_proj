

#-----main-----
a, b, c = input().split() #split input

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"): #if a and b cancel each other out
    print("No")
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"): #if b and c cancel each other out
    print("No")
else:
    print("Yes")
