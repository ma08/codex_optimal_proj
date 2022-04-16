
import math

V = int(input())

a = int(math.ceil(V**(1/3)))
b = int(math.ceil((V/a)**(1/2)))
c = int(math.ceil(V/(a*b)))

print(2*(a*b + b*c + a*c))
