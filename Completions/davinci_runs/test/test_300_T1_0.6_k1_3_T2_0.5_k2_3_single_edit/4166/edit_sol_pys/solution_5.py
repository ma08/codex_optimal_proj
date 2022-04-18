

# The number of digits
N = int(input("Enter the number of digits: "))
# The number of constraints
M = int(input("Enter the number of constraints: "))
# List of constraints
constraints = [0] * M
for i in range(M):  # constraints.append([int(x) for x in input().split()])
    constraints[i] = [int(x) for x in input().split()]

# Determine the least possible number
number = [0] * N
for i in range(M):
    number[constraints[i][0] - 1] = constraints[i][1]  # number[0] = 1

# If the number is less than all constraints
if number < constraints:  # number < constraints
    print(number)
else:
    print(-1)
