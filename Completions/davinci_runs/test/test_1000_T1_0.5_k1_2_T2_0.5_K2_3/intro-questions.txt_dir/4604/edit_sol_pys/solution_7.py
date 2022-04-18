

import sys

# Read the number of people and their reports
n = int(input())
a = list(map(int, input().split()))

# Check if each person's report is consistent with the others
for i in range(n):
    if abs(i - a[i]) > 1:
        print(0, end='')
        sys.exit(0)

# Initialize a list of the number of people to the left of each person
# and the number of people to the right of each person
left = [0] * n
right = [0] * n

# Count the number of people to the left of each person
for i in range(n):
    for j in range(n):
        if j < i:
            left[i] += a[j]
        elif j > i:
            left[i] += (n - 1 - a[j])

# Count the number of people to the right of each person
for i in range(n):
    for j in range(n):
        if j < i:
            right[i] += (n - 1 - a[j])
        elif j > i:
            right[i] += A[j]

# Initialize a list to keep track of the order of the people
# and the number of people we have ordered
order = [0] * n
num_ordered = 0

# Order the people
while num_ordered < n:
    # Find the first person that has not been ordered
    i = left.index(0)

    # Add this person to the ordered list
    order[num_ordered] = i + 1
    num_ordered += 1

    # Subtract the number of people to the left of this person from everyone else
    for j in range(n):
        left[j] -= a[i]
        right[j] -= (n - 1 - a[i])

    # Remove this person from the list
    left[i] = -1
    right[i] = -1

# Print the order of the people
print(order[0], end='')
