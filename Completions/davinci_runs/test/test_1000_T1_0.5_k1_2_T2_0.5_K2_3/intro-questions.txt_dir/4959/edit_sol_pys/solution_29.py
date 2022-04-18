
e,f,c=map(int,input().split())

bottles = e + f
drinks=0

while bottles >= c:
    drinks+=bottles//c
    bottles=bottles%c+bottles//c

print (drinks)
