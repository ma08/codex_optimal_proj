
a,b,c = map(int,input().split()) # input the sides of a triangle
s = (a+b+c)/2 # calculate the semi-perimeter
print(int(s*(s-a)*(s-b)*(s-c))**(1/2)) # calculate the area using Heron's formula
