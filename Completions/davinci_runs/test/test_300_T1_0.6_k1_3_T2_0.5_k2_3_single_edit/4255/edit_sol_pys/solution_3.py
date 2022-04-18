
import sys

def area(a, b, c): 
    s = (a+b+c)/2 
    return (s*(s-a)*(s-b)*(s-c))**0.5 
  
# Driver Code 
a = 3
b = 4
c = 5
print('The area of the triangle is %0.2f' %area(a, b, c)) 
