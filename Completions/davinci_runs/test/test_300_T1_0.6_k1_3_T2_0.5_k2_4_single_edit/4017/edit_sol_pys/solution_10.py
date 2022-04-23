


"""
Good luck!
"""

# SOLUTION
n = int(input())
a = list(map(int, input().split()))

# check if the array is good
if sum(a) - max(a) == max(a):
    print(1)
    print(a.index(max(a))+1)
else:
    print(0)
