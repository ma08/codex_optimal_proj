
# Solution:

a,b,c = input().split()
a,b,c = int(a),int(b),int(c)
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
