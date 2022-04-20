

#import sys

#n, m = map(int, sys.stdin.readline().split())
#a = []

#for i in range(n):
#    a.append(list(map(int, sys.stdin.readline().split())))

#for i in range(1, m+1):
#    for j in range(n):
#        if i in a[j]:
#            continue
#        else:
#            break
#    else:
#        print(i)

#print(a)

#n, m = map(int, input().split())
#a = []
#for i in range(n):
#    a.append(list(map(int, input().split())))
#print(a)

#for i in range(1, m+1):
#    for j in range(n):
#        if i in a[j]:
#            continue
#        else:
#            break
#    else:
#        print(i)

n, m = map(int, input().split())
a = []
for i in range(n):
    a.append(list(map(int, input().split())))

#print(a)

for i in range(1, m+1):
    for j in range(n):
        if i in a[j]:
            continue
        else:
            break
    else:
        print(i)