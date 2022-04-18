

# get the number of people
n = int(input())

# get the number of teams
m = int(input())

# initialize the number of ways to make teams
num_ways = 1

# loop over the number of people
for i in range(n):
    # set the number of ways to make teams
    num_ways *= m

# print the answer
print(num_ways)
