
N = int(input()) #input a number
if N % 2 == 0 and N > 2: #check if the number is even and greater than 2
    print("Yes") #print "Yes"
elif N % 3 == 0 and N > 3: #check if the number is divisible by 3 and greater than 3
    print("Yes") #print "Yes"
elif N % 5 == 0 and N > 5: #check if the number is divisible by 5 and greater than 5
    print("Yes") #print "Yes"
elif N % 7 == 0 and N > 7: #check if the number is divisible by 7 and greater than 7
    print("Yes") #print "Yes"
else:
    print("No") #print "No"
