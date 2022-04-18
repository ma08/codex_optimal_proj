

# This problem is solved by using the sorted() function
# sorted() takes in a list and returns a list of all unique values

# Gets input
N = int(input())
S = [input() for i in range(N)]

# Sorts the list
S = sorted(S)

# Prints the sorted list
for i in S:
    print(i)
