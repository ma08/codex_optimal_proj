

# cook your dish here
def find(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    elif n==3:
        return 2
    elif n%2==0:
        return 1+find(n//2)
    elif n%3==0:
        return 1+find(n//3)
    else: 
        return 1+find(n-1)

test=int(input())
for i in range(test):
    n=int(input())
    print(find(n))
