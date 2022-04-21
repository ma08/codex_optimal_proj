

t = int(input())

for i in range(t):
    n = int(input())


#did this
def fun(a,b,c):
    if a < b:
        if a < c:
            if b < c:
                return b
            else:
                return c
        else:
            return a
    else:
        if b < c:
            if a < c:
                return a
            else:
                return c
        else:
            return b
    print(n//2)
