
# Gets input
N = int(input())
S = [input() for i in range(N)]

# Sets all values in S to lowercase
S = [i.lower() for i in S]

# Creates a list of the unique values in S
unique = list(set(S))

# Sorts the list
unique.sort()

# Prints the list
for i in unique:
    print(i)
