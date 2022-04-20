
S = input()
T = input()

changes = 0 # initialize the number of changes needed

for i in range(len(S)): # iterate through the string
    if S[i] != T[i]: # if the current character in S does not match the current character in T
        changes += 1 # increment the number of changes needed

print(changes) # print the number of changes needed
