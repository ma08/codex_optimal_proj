

#-----main-----
a, b, c = input().split() #split input into 3 strings

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"): #if first 2 strings are opposite
    print("No") #output No
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"): #if last 2 strings are opposite
    print("No") #output No
else:
    print("Yes")
