

import itertools

n = int(input()) #number of folders
s = list(map(int, input().split())) #number of pages in each folder

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
