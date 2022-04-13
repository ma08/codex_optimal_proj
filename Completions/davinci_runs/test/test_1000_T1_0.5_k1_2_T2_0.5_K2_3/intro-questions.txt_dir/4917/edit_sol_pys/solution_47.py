

#cook your dish here

a = []
b = []
c = []
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=c[i]:
            return False
    return True

for i in range(N):
    x,y = map(int,input().split())
    a.append(x)
    b.append(y)
    c.append(x+y)
    if check(x):
        print("gunilla has a point")
        break
else:
    print("edward is right")
