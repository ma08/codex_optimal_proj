

n=int(input())
s=input()

def count(n,s):
    
    if n==0:
        return 1
    elif len(s)==0:
        return 0
    elif s[0]=='(':
        return count(n-1,s[1:])+count(n,s[1:])
    else:
        return count(n,s[1:])

print(count(n,s))