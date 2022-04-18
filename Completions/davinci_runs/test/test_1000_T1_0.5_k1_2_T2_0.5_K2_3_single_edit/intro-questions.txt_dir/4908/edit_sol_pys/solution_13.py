
import math
a=int(input())
b=int(input())
c=int(input())
if c==a+b:
    print (str(a)+"+"+str(b)+"="+str(c))
elif c==a-b:
    print (str(a)+"-"+str(b)+"="+str(c))
elif c==a*b:
    print (str(a)+"*"+str(b)+"="+str(c))
elif c==a/b:
    print (str(a)+"/"+str(b)+"="+str(c))
elif c==b/a:
    print (str(b)+"/"+str(a)+"="+str(c))
elif c==a/math.gcd(a,b):
    print (str(a)+"/"+str(math.gcd(a,b))+"="+str(c))
elif c==b/math.gcd(a,b):
    print (str(b)+"/"+str(math.gcd(a,b))+"="+str(c))
