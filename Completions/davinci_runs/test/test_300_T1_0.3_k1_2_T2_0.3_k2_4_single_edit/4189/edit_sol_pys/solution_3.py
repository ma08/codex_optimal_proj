
# SOLUTION

n = int(input())

soft = []
hard = []

for i in range(n):
    cheese, type_of_cheese = input().split()
    if type_of_cheese == 'soft':
        soft.append(cheese)
    else:
        hard.append(cheese)

print(len(soft))
