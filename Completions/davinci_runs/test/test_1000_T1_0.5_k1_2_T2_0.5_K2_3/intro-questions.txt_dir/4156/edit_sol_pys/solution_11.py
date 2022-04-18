n,w=map(int,input().split()) #input n and w
a=list(map(int,input().split())) #input a
if sum(a)>w or sum(a)<-w or sum(a)+w<0 or sum(a)-w>0: #if sum of a is greater than w or less than -w or sum of a plus w is less than 0 or sum of a minus w is greater than 0
    print(0) #print 0
else: #else
    print(w-abs(sum(a))) #print w minus the absolute value of sum of a
