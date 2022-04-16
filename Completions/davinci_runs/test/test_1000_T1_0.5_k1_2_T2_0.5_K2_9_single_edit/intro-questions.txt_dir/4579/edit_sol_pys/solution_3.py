

# This problem is solved by using the set() function set() takes in a list
# and returns a list of all unique values

# Gets input from user

# Creates a list of the input
N = int(input())
S = [input() for i in range(N)]

# Gets the number of unique values and prints it
print(len(set(S)))
