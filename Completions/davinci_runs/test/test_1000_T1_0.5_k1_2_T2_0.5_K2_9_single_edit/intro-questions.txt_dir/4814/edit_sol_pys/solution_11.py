#!/usr/bin/env python3

# Gets the number of people on the team
n = int(input())

# Gets the names of each person on the team
names = []
for i in range(n):
    name = input()
    names.append(name)

# Sorts the names into alphabetical order
ordered = sorted(names)

# If the names are in alphabetical order and the names are in reverse alphabetical order,
# the list is neither in increasing or decreasing alphabetical order.
# Otherwise, it is either in increasing or decreasing alphabetical order.
if names == ordered:
    print("INCREASING")
elif names == ordered[::-1]:
    print("DECREASING")
else:
    print("NEITHER")
