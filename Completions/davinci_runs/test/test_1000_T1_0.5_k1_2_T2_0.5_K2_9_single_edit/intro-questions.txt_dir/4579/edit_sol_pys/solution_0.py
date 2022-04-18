

# This problem is solved by using the set() function
# set() takes in a list and returns a list of all unique values

# Gets input and stores in a list
N = int(input())
S = [input() for i in range(N)]

# Gets the number of unique values
print(len(set(S)))
