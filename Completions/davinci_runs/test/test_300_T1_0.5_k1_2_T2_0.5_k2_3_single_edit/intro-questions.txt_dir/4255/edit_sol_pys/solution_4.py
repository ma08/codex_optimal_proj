
#take three sides of a triangle as input
import math

#assign values to each side
abc = input().split()
a, b, c = int(abc[0]), int(abc[1]), int(abc[2])
#check if a is the largest side
    #check if b is the second largest side
if a >= b and a >= c:
    if b >= c:
        p = (a + b + c) / 2
    #check if c is the second largest side
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    else:
        p = (a + b + c) / 2
#check if b is the largest side
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    #check if a is the second largest side
elif b >= a and b >= c:
    if a >= c:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    #check if c is the second largest side
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
#check if c is the largest side
else:
    #check if a is the second largest side
    if a >= b:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
    #check if b is the second largest side
    else:
        p = (a + b + c) / 2
        print(math.sqrt(p * (p - a) * (p - b) * (p - c)))
