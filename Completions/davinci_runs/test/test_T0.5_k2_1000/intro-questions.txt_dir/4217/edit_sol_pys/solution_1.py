

N, M = map(int, input().split())  # Get the input

A = []  # Initialize the list

# Get the input
for i in range(N):
    A.append(list(map(int, input().split())))

# Initialize the counter to 0
count = 0

# Iterate through all the foods from 1 to M
for i in range(1, M + 1):
    # Iterate through all the people from 0 to N - 1
    for j in range(N):
        # If the food is not in the list of liked foods of the person
        # Break the loop and go to the next food
        if i not in A[j][1:]:
            break
    # If the food is in the list of liked foods of all the people,
    # Increment the counter by 1
    else:
        count += 1

print(count)
