

#-----main-----#
a, b, c = input().split() #input

if (a == "North" and b == "South") or (a == "South" and b == "North") or (a == "East" and b == "West") or (a == "West" and b == "East") or (a == "North" and c == "South") or (a == "South" and c == "North") or (a == "East" and c == "West") or (a == "West" and c == "East"): #if a and b are opposite
    print("No") #print no
else: #if a and b are not opposite or a and c are not opposite
    print("Yes") #print yes
