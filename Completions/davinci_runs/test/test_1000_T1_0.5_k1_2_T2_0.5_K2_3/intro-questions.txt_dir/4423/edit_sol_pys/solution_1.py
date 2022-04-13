
n = int(input())
d = {} # create a dictionary
for i in range(n): # run n times to get n inputs
    s, p = input().split() # get input, split it by space
    p = int(p) # change the type of p from string to integer
    if s not in d.keys(): # if s is not in the dictionary d
        d[s] = [p] # add s as key and p as value to d
    else: # if s is already in the dictionary d
        d[s].append(p) # add p as value to d

for s in sorted(d.keys()): # sort the dictionary d by key
    d[s].sort(reverse=True) # sort the values by descending order, and assign them back to d

for s in sorted(d.keys()): # sort the dictionary d by key
    for p in d[s]: # for each value in d
        print(p) # print the value in d
