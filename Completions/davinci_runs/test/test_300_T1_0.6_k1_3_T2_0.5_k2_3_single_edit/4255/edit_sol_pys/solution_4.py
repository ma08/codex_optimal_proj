
import math
a,b,c = map(int,input().split())

# Heron's formula
def area(a,b,c):
  s = (a+b+c)/2
  return (s*(s-a)*(s-b)*(s-c))**0.5


print(int(area(a,b,c)))
