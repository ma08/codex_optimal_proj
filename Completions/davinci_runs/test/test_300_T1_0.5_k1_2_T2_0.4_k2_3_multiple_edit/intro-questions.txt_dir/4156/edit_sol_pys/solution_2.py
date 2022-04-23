n,w=map(int,input().split()) #n=number of elements in a array and w=weight
a=list(map(int,input().split())) #a=array
if sum(a)>w or sum(a)<-w or sum(a)+w<0 or sum(a)-w>0: #if sum of elements is greater than w or less than w or sum of elements is less than 0 or sum of elements is greater than 0
    print(0) #print 0
else: #else
    print(w-abs(sum(a))) #print weight-sum of elements
