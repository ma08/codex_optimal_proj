

#cook your dish here
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=b[i] or a[i]>=b>=b[i]:
            return False
    return True
a = []
b = []

for i in range(N):
    a1,b1 = map(int,input().split())
    a.append(a1)
    b.append(b1)
    if check(a1):
        print("Gunilla has a point")
        break
else:
    print("Edward is right")
