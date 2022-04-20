

a,b,c = map(int,input().split())

# Heron's formula for calculating area of a triangle
def area(a,b,c):
    s = (a+b+c)/2
    return (s*(s-a)*(s-b)*(s-c))**(1/2)


print(int(area(a,b,c)))
