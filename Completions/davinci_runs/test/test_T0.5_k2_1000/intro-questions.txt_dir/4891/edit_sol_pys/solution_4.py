

pcs = [int(x) for x in input().split()]  # input the numbers

for i in range(len(pcs)):  # for loop
    if i == 0:
        if pcs[i] > 1:  # if the number is greater than 1
            pcs[i] = pcs[i] - 1
        elif pcs[i] < 1:  # if the number is less than 1
            pcs[i] = pcs[i] + 1
    elif i == 1:
        if pcs[i] > 1:  # if the number is greater than 1
            pcs[i] = pcs[i] - 1
        elif pcs[i] < 1:  # if the number is less than 1
            pcs[i] = pcs[i] + 1
    elif i == 2:
        if pcs[i] > 2:  # if the number is greater than 2
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:  # if the number is less than 2
            pcs[i] = pcs[i] + 2
    elif i == 3:
        if pcs[i] > 2:  # if the number is greater than 2
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:  # if the number is less than 2
            pcs[i] = pcs[i] + 2
    elif i == 4:
        if pcs[i] > 2:  # if the number is greater than 2
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:  # if the number is less than 2
            pcs[i] = pcs[i] + 2
    elif i == 5:
        if pcs[i] > 8:  # if the number is greater than 8
            pcs[i] = pcs[i] - 8
        elif pcs[i] < 8:  # if the number is less than 8
            pcs[i] = pcs[i] + 8

print(*pcs)  # print the new list
