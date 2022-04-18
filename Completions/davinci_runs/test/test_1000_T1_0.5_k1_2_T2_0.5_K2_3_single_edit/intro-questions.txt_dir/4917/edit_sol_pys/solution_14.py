

#program to check if the given intervals overlap

n = int(input())                                 #number of intervals

l = []                                           #list to store intervals

for i in range(n):                               #taking input
    l.append(list(map(int,input().split())))     #appending to the list

l.sort(key=lambda x: x[1])                       #sorting the list by the lower limit of the interval

if l[0][1] >= l[1][0]:                           #checking if the intervals overlap
    print("gunilla has a point")                 #if they overlap
else:
    print("edward is right")                     #if they don't overlap
