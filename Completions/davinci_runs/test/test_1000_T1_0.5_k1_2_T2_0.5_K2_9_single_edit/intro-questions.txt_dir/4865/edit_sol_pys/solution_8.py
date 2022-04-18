
import math
a,b,c = map(int, input().split())
if b**2 - 4*a*c < 0:
    print("No real roots")
elif b**2 - 4*a*c == 0:
    print("Two same roots x=",int(-b/(2*a)))
else:
    print("Two different roots x1=",int((-b + math.sqrt(b**2 - 4*a*c))/(2*a))," , x2=",int((-b - math.sqrt(b**2 - 4*a*c))/(2*a)))
