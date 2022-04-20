
# SOLUTION

n = int(input())
soft, hard = [], []

for i in range(n):
    cheese, type = input().split()
    if type == 'soft':
        soft.append(cheese)
    else:
        hard.append(cheese)

print(len(soft))
