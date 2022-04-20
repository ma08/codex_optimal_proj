

# SOLUTION

n,x,y = map(int,input().split())
s = input()

if s[:x] == '1'*x:
    if s[x:x+y] == '0'*y:
        print(0)
    else:
        print(1)
else:
    print(x-y)