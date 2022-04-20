

n = int(input())

soft = []
hard = []

for i in range(n):
    cheese, type = input().split() # split the input by space
    if type == 'soft':
        soft.append(cheese)
    else:
        hard.append(cheese)

print(len(soft))
