

S = input()
T = input()

# initialize the number of changes needed and the current index
changes = 0 
index = 0

# iterate through the string, starting at the current index
for i in range(len(S)):
    if S[index] != T[index]:
        # increment the number of changes needed
    index += 1
        changes += 1

# print the number of changes needed
print(changes)
