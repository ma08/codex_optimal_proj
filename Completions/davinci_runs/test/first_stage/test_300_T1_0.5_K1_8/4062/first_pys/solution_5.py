

a,b,c,d = map(int,input().split())

# x,y = b,d
# x,y = a,d
# x,y = b,c
# x,y = a,c

if a <= c:
    x = b
    y = d
    print(x*y)
elif a > c:
    x = a
    y = d
    print(x*y)