
def check(a,b,c):
    if a+b==c:
        return "True"
    elif a-b==c:
        return "True"
    elif a*b==c:
        return "True"
    elif a/b==c:
        return "True"
    elif a==b+c:
        return "True"
    elif a==b-c:
        return "True"
    elif a==b*c:
        return "True"
    elif a==b/c:
        return "True"
    else:
        return "False"

a,b,c = map(int,input().split())
print(check(a,b,c))
