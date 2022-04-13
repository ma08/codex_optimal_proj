
N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# Print the list of foods liked by all the N people.

for i in range(N):
    for j in range(A[i][0]):
        print(A[i][j + 1], end=' ')
    print()

# Find the number of the foods liked by all the N people.

# Initialize the variable to 0
count = 0

# Iterate through all the foods.
for i in range(1, M + 1): # Iterate through all the people.
    for j in range(N): # If the food is not in the list of liked foods
        if i not in A[j][1:]: # of the person, break the loop and go to the next food.
            break # If the food is in the list of liked foods of all the people.
    else: # Increment the count by 1.
        count += 1 # Print the number of foods liked by all the N people.

print(count)
