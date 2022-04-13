# Code for the problem

n = int(input())
names = []
for _ in range(n):
    names.append(input())

if names == sorted(names, reverse=True):
    print("INCREASING")
elif names == sorted(names):
    print("DECREASING")
else:
    print("NEITHER")
