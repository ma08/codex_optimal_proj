

#Solution

# cook your dish here
for i in range(int(input())):
    s=input()
    m=int(input())
    b=list(map(int,input().split()))
    l=[]
    for j in range(len(s)):
        l.append(s[j])
    l.sort()
    t=[]
    for j in range(len(s)):
        t.append('')
    for j in range(len(s)):
        if(b[j]==0):
            t[j]=l[0]
            l.remove(l[0])
        else:
            t[j]=l[len(l)-1]
            l.remove(l[len(l)-1])
    print(''.join(t))