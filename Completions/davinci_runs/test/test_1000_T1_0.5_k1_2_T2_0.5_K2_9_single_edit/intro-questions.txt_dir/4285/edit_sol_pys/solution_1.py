
import sys, string, math
n = int(input())
L = list(map(int,input().split()))
for i in range(len(L)) :
    if L[i] > 0 :
        if i%2 == 0 :
            print(i,end=' ')
