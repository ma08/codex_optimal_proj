

n,m=map(int,input().split())
a=list(map(int,input().split()))

# a=[2,3,1,1,2]
# m=8

def get_cups(a,m):
    cups=0
    for i in range(len(a)):
        cups+=a[i]
        if cups>=m:
            return i+1
    return -1

def get_days(a,m):
    days=0
    while True:
        days+=1
        cups=get_cups(a,m)
        if cups>0:
            for i in range(cups):
                a[i]-=cups-i
            m-=cups
            a=a[cups:]
        else:
            return -1
        if m<=0:
            return days

print(get_days(a,m))