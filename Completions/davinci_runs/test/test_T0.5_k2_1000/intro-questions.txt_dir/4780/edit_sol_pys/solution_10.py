

# SOLUTION

n1, n2 = map(int, input().split())  # read input

row1 = input()  # read input
row2 = input()

t = int(input())  # read input

row1 = list(row1)  # convert to list
row2 = list(row2)

for i in range(t):  # loop t times
    if len(row1) > 0 and len(row2) > 0:  # check if both rows are not empty
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
