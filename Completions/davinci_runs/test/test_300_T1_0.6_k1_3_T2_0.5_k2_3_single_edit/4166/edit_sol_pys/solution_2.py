

#The number of digits in the number
N = int(input())
#The number of constraints
M = int(input())
#List of constraints
constraints = []
for i in range(M):
    constraints.append([int(x) for x in input().split()]) #read constraints

#Determine the least possible number from the constraints
number = [0] * N
for i in range(M):
    number[constraints[i][0] - 1] = constraints[i][1]

#If the number is less than or equal to all constraints
if number <= constraints:
    print(number)
else:
    print(-1)
