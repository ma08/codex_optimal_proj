

# cook your dish here.
n=int(input())
s=input()
t=input()
if(s==t):
    print(0)
    print()
else:
    if(len(set(s))!=len(set(t)) or len(set(s))!=len(set(t))):
        print(-1)
    else:
        i=0
        j=1
        c=0
        moves=[]
        while(i<n-1 and j<n):
            if(s[i]!=t[i]):
                if(s[j]==t[i]):
                    s=s[:i]+s[j]+s[i+1:j]+s[i]+s[j+1:] #swap
                    moves.append(i)
                    c+=1
                else:
                    j+=1
            elif(s[i]==t[i] and s[j]==t[j]):
                i+=1
                j+=1
            else:
                i+=1
                j=i+1
        if(s==t):
            print(c)
            for i in moves:
                print(i+1,end=" ")
            print()
        else:
            print(-1)
