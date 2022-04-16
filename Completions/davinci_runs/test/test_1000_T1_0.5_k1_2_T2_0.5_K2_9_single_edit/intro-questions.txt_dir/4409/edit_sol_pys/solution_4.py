

# cook your dish here
for _ in range(int(input())):
    n=int(input())
    s=input()
    d={}
    for i in s:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    p=0
    for i in d:
        if d[i]%2==0:
            p+=1
    if p%2==0:
        print("Player2")
    else:
        print("Player1")
