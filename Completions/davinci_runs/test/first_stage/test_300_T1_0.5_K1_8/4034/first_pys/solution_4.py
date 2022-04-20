

# cook your dish here
t=int(input())
s=input()
if t==1:
    print("YES")
    print("0")
else:
    if s[0]>s[1]:
        print("YES")
        print("1",end="")
        for i in range(1,t-1):
            if s[i]<s[i-1] and s[i]<s[i+1]:
                print("1",end="")
            else:
                print("0",end="")
        if s[t-1]<s[t-2]:
            print("1")
        else:
            print("0")
    else:
        print("YES")
        print("0",end="")
        for i in range(1,t-1):
            if s[i]>s[i-1] and s[i]>s[i+1]:
                print("0",end="")
            else:
                print("1",end="")
        if s[t-1]>s[t-2]:
            print("0")
        else:
            print("1")