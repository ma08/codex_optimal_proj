import collections

N = int(input())
A = list(map(int, input().split()))

# print(A)

# Initialize the dictionary
d = collections.defaultdict(int)

# Iterate through the list of integers
for i in A:
    # Increment the count of each integer by 1
    d[i] += 1

# print(d)

# Find the number of integers that appear an odd number of times
count = 0
for i in d:
    if d[i] % 2 != 0:
        count += 1

print(count)


N, M = map(int, input().split())

A = []
for i in range(N):
    A.append(list(map(int, input().split())))

# print(A)

# for i in range(N):
#     for j in range(A[i][0]):
#         print(A[i][j + 1], end=' ')
#     print()

# Find the number of the foods liked by all the N people.

# Initialize the variable to 0
count = 0

# Iterate through all the foods
for i in range(1, M + 1):
    # Iterate through all the people
    for j in range(N):
        # If the food is not in the list of liked foods
        # of the person, break the loop and go to the next food
        if i not in A[j][1:]:
            break
    # If the food is in the list of liked foods of all the people
    # Increment the count by 1
    else:
        count += 1

print(count)
