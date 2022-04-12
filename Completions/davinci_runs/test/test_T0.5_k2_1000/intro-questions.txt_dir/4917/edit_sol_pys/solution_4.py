

#cook your dish here
N = int(input())

def check(b):
    for i in range(N):
        if a[i]<=b<=c[i]:
            return False
    return True

for i in range(N):
    a[i],b[i] = map(int,input().split())
    if check(b[i]):
        print("gunilla has a point")
        break
else:
    print("edward is right")
