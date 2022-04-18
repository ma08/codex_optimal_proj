
from itertools import product

a,b,c,d = map(int,input().split())

valid = []

for p in product(['+','-','*','/'],repeat=2):
    if eval(str(a)+p[0]+str(b) == str(c)+p[1]+str(d)):
        valid.append(str(a)+" "+p[0]+" "+str(b)+" = "+str(c)+" "+p[1]+" "+str(d))

valid.sort()

if valid:
    for v in valid:
        print(v)

else:
    print("problems ahead")
