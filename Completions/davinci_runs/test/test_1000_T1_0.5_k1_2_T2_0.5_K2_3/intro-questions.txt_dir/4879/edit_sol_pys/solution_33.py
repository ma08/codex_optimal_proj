
#-----main-----
a, b, c = input().split()

if a == "South" and b == "North":
    print("No") 
elif c == "North" and b == "South":
    print("No") 
elif a == "East" and b == "West":
    print("No") 
elif c == "West" and b == "East":
    print("No") 
else:
    print("Yes")
