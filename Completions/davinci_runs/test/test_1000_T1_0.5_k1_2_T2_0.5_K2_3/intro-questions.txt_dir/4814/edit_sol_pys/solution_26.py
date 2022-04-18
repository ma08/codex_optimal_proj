# Code for the problem

n = int(input()) #number of names
names = [] #list of names
for _ in range(n): #for loop to fill list with names
    names.append(input()) #add name to list

if names == sorted(names):
    print("INCREASING")
elif names == sorted(names, reverse=True):
    print("DECREASING")
else:
    print("NEITHER")
