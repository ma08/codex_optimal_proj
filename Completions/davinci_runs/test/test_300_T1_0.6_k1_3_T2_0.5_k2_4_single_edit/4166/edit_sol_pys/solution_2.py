

#The number of digits
N = int(input())
#The number of constraints
M = int(input())
#List of constraints
constraints = []
for i in range(M):
    constraints.append([int(x) for x in input().split()])

#Determine the least possible number
number = [0] * N
for i in range(M):
    number[constraints[i][0] - 1] = constraints[i][1]

#If the number is less than all constraints
if number < constraints[0]:
    print(str(number))
else:
    print(-1)
