# Get input
S = input()
T = input()

# Set up variables
slen = len(S)
tlen = len(T)

# Initialize array to store the minimum number of changes needed
changes = [[0 for i in range(slen + 1)] for j in range(tlen + 1)]

# Populate the first row
for i in range(1, slen + 1):
    changes[0][i] = i

# Populate the first column
for j in range(1, tlen + 1):
    changes[j][0] = j

# Calculate the rest of the matrix
for j in range(1, tlen + 1):
    for i in range(1, slen + 1):
        if S[i-1] == T[j-1]:
            changes[j][i] = changes[j-1][i-1]
        else:
            changes[j][i] = min(changes[j-1][i], changes[j][i-1], changes[j-1][i-1]) + 1

print(changes[tlen][slen])



# Get input
S = input()
T = input()

# Set up variables
slen = len(S)
tlen = len(T)

# Initialize array to store the minimum number of changes needed
changes = [[0 for i in range(slen + 1)] for j in range(tlen + 1)]

# Populate the first row
for i in range(1, slen + 1):
    changes[0][i] = i

# Populate the first column
for j in range(1, tlen + 1):
    changes[j][0] = j

# Calculate the rest of the matrix
for j in range(1, tlen + 1):
    for i in range(1, slen + 1):
        if S[i-1] == T[j-1]:
            changes[j][i] = changes[j-1][i-1]
        else:
            changes[j][i] = min(changes[j-1][i], changes[j][i-1], changes[j-1][i-1]) + 1

print(changes[tlen][slen])
