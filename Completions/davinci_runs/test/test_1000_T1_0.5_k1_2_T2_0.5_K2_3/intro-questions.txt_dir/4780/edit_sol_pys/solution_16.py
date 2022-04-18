
# SOLUTION
n1, n2 = map(int, input().split())  # input two numbers
row1 = input()  # input the first row
row2 = input()  # input the second row
t = int(input())  # input the number of time to perform the operation
row1 = list(row1)  # convert the string into list
row2 = list(row2)  # convert the string into list
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
