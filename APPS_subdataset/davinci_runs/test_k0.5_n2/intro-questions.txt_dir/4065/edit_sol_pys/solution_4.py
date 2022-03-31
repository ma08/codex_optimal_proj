
n = int(input()) # number of elements
a = [int(x) for x in input().split()] # elements

contest = [] # list of elements

for i in range(n):
    
    if len(contest) == 0: # if list is empty
        contest.append(a[i])
    elif a[i] <= contest[-1] * 2: # if element is less than double of last element
        contest.append(a[i])
    else: # if element is greater than double of last element
        contest = [a[i]]

print(len(contest))
