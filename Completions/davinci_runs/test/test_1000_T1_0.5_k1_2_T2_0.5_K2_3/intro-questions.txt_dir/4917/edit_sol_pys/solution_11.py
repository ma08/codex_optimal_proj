

#cook your dish here
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=c[i]:
            return False
    return True

for i in range(N):
    a,c = map(int,input().split())
    if check(a):
        print("Gunilla has a point")
        break
else:
    print("Edward is right")
