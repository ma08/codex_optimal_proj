
# Gets the number of people on the team
n = int(input())

# Gets the names of each person on the team and sorts them into alphabetical order
names = sorted([input() for i in range(n)])

# If the names are in alphabetical order and the names are in reverse alphabetical order, the list is neither in increasing or decreasing alphabetical order. Otherwise, it is either in increasing or decreasing alphabetical order.
if names == sorted(names):
    print("INCREASING")
elif names == sorted(names)[::-1]:
    print("DECREASING")
else:
    print("NEITHER")
