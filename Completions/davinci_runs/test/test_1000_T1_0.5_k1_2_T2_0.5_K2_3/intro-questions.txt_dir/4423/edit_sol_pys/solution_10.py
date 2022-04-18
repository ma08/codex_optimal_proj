n = int(input()) # number of input
d = {}
for i in range(n): # run n times
    s, p = input().split() # input s and p for each time
    p = int(p) # change the type of p from str to int
    if s not in d.keys(): # if s is not in the dictionary
        d[s] = [p] # add s as key and p as value
    else:
        d[s].append(p) # add p as value

for s in sorted(d.keys()): # sort the dictionary by key
    d[s].sort(reverse=True) # sort the values by descending order

for s in sorted(d.keys()): # sort the dictionary by key
    for p in d[s]: # for each value
        print(p) # print the value
