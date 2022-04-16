

#Solution:

a,b,c = input().split()
a,b,c = float(a),float(b),float(c)
if a+b==c:
    print(str(a)+"+"+str(b)+"="+str(c))
elif a-b==c:
    print(str(a)+"-"+str(b)+"="+str(c))
elif a*b==c:
    print(str(a)+"*"+str(b)+"="+str(c))
elif a/b==c:
    print(str(a)+"/"+str(b)+"="+str(c))
elif a==b+c:
    print(str(a)+"="+str(b)+"+"+str(c))
elif a==b-c:
    print(str(a)+"="+str(b)+"-"+str(c))
elif a==b*c:
    print(str(a)+"="+str(b)+"*"+str(c))
elif a==b/c:
    print(str(a)+"="+str(b)+"/"+str(c))
