

#cook your dish here
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=b[i] and b[i]<=b<=a[i]:
            return False
    return True

for i in range(N):
    a,b = map(int,input().split())
    if check(a):
        print("gunilla has a point")
        break
else:
    print("edward is right")
