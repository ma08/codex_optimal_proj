from itertools import product
a,b,c,d = map(int,input().split())
valid = []
for p in product(['+','-','*','/'],repeat=2):
    if eval("{0}{1}{2} == {3}{4}{5}".format(a,p[0],b,c,p[1],d)):
        valid.append("{0} {1} {2} = {3} {4} {5}".format(a,p[0],b,c,p[1],d))
valid.sort()
if valid:
    for v in valid:
        print(v)
else:
    print("problems ahead")
