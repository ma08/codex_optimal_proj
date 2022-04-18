

import math as m

N = int(input()) #input

moves = 0 #set moves to 0

for i in range(1,N+1): #loop through
    if(m.pow(i,2) >= N): #if i^2 >= N
        moves = i #set moves to i
        break #break out of loop

print(2*moves-2) #print 2*moves-2
