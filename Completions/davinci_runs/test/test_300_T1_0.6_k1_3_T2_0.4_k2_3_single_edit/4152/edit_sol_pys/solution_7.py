
import math
n = int(input()) #no of boxes
l = list(map(int,input().split())) #list of items in each box
c = Counter(l)
c1 = []
for i in range(len(c)):
    c1.append(c[i])
print(n-max(c.values()))
