

from itertools import combinations

def count(n, k, a):
    for i in combinations(a, 2):
        if i[0]+i[1]%k==0:
            return "YES"
        else:
            return "NO"

n, k = map(int, input().split()) #Get n, k
a = [int(x) for x in input().split()] #Get array a
print(count(n, k, a)) #Print result
