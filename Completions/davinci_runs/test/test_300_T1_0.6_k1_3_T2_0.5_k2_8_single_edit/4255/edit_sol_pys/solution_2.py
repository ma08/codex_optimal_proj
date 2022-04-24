
from math import sqrt
a,b,c = map(int,input().split())

# Heron's formula
def area(a,b,c):
  s = (a+b+c)/2
  return sqrt(s*(s-a)*(s-b)*(s-c))


print(int(area(a,b,c)))
