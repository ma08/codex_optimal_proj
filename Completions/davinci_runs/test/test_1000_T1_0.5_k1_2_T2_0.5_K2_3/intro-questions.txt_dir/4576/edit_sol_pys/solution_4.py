

# get inputs
S = input()
T = input()

# convert the strings to lists
S = list(S)
T = list(T)

# loop over all indices of the lists
for i in range(len(S)):
    # check if the characters at the current indices are the same
    if S[i] == T[i]:
        # convert the characters to '*'
        S[i] = '*'
        T[i] = '*'

# convert the lists to strings and print the strings
print(''.join(S))
print(''.join(T))
