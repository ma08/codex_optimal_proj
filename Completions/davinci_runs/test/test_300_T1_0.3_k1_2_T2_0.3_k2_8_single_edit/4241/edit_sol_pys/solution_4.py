
S = input()
T = input()

# initialize the number of changes needed
changes = 0

# iterate through the string
for i in range(len(S)):
    # if the current character in S does not match the current character in T
    if S[i] != T[i]:
        # increment the number of changes needed
        changes += 1

# print the number of changes needed
print(changes)
