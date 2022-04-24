

# SOLUTION
n = int(input()) # number of elements in the array
a = list(map(int, input().split())) # the array

# check if the array is good
if sum(a) - max(a) == max(a):
    print(1)
    print(a.index(max(a))+1)
else:
    print(0)

"""
Good luck!
"""
