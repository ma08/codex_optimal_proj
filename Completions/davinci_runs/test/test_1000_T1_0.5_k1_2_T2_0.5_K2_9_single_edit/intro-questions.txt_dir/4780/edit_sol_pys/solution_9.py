

# SOLUTION

n1, n2 = map(int, input().split()) # Take input

row1 = input() # Take input
row2 = input() # Take input

t = int(input()) # Take input

row1 = list(row1) # Convert to list
row2 = list(row2) # Convert to list

for i in range(t):
    if len(row1) > 0 and len(row2) > 0:
        if row1[0] < row2[0]:
            row1.append(row1[0])
            row1.append(row2[0])
            row1.pop(0)
            row2.pop(0)
        else:
            row2.append(row2[0])
            row2.append(row1[0])
            row2.pop(0)
            row1.pop(0)

print(''.join(row1 + row2))
