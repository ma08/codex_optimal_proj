

# This is a combinatorics problem. 
# The only problem is that the solution is not necessarily unique. 
 
import itertools
 
n = int(input())
 
s = list(map(int, input().split()))
 
def is_safe(order):
    students = 0
    for i in order:
        students += s[i-1]
        if students > sum(s):
            return False
    return True
 
 
def is_safe_unique(order):
    students = 0
    for i in order:
        students += s[i-1]
        if students > sum(s):
            return False
        if students == sum(s):
            return True
    return True
 
 
for order in itertools.permutations(range(1, n+1)):
    if is_safe(order):
        print(" ".join(map(str, order)))
        break
else:
    print("impossible")
