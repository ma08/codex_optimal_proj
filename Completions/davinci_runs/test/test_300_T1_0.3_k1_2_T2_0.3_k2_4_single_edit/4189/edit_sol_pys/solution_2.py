
# SOLUTION

n = int(input())

soft = []
hard = []

for i in range(n):
    cheese, cheese_type = input().split()
    if cheese_type == 'soft':
        soft.append(cheese)
    else:
        hard.append(cheese)

print(len(soft))
