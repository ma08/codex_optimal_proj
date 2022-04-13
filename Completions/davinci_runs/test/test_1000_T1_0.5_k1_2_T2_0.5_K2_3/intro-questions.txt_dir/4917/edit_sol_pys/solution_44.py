

#cook your dish here
N = int(input())
a = []
b = []
def check(b):
    for i in range(N):
        if a[i]<=b<=c[i]:
            return False
    return True

for i in range(N):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
    if check(b1):
        print("gunilla has a point")
        break
else:
    print("edward is right")
