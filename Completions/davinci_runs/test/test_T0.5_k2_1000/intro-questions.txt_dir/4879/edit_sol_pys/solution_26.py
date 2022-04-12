
#-----main-----#
a, b, c = input().split() #input

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East"): #if a and b are opposite
    print("No") #print no
elif (c == "North" and b == "South") or (c == "South" and b == "North") or (c == "East" and b == "West") or (c == "West" and b == "East"): #if b and c are opposite
    print("No") #print no
else: #if a and b are not opposite
    print("Yes") #print yes
