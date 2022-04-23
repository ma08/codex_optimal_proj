

# cook your dish here.
def find(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else: 
        return find(n-1)+find(n-2)+find(n-3)

test=int(input())
for i in range(test):
    n=int(input())
    print(find(n))
