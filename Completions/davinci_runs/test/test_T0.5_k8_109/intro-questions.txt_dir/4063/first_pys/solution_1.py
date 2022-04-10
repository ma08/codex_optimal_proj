

# -----Solution-----

n = int(input())
difficulties = list(map(int, input().split()))

difficulties.sort()

# We know that n is even, so we can just round down and round up
# the middle two numbers and compare them to the rest of the list
# to get the number of choices for K that make the number of problems
# for ARCs and the number of problems for ABCs the same.
# This is O(n) time complexity.

# This is the number of choices for K that make the number of problems
# for ARCs and the number of problems for ABCs the same.
num_choices = 0

mid_num_1 = difficulties[(n//2)-1]
mid_num_2 = difficulties[n//2]

# The number of problems for ARCs and ABCs are the same when K is equal to
# the lower of the two middle numbers.
if mid_num_1 == mid_num_2:
    num_choices = 1

# The number of problems for ARCs and ABCs are the same when K is equal to
# the lower of the two middle numbers or the higher of the two middle numbers.
elif mid_num_1 + 1 == mid_num_2:
    num_choices = 2

print(num_choices)