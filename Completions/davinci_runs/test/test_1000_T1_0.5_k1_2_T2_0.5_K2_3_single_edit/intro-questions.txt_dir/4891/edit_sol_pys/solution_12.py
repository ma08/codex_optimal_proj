

pcs = [int(x) for x in input().split()] # input of numbers

for i in range(len(pcs)): # iterate through the list
    if i == 0:
        if pcs[i] > 1:
            pcs[i] = pcs[i] - 1
        elif pcs[i] < 1:
            pcs[i] = pcs[i] + 1
    elif i == 1:
        if pcs[i] > 1:
            pcs[i] = pcs[i] - 1
        elif pcs[i] < 1:
            pcs[i] = pcs[i] + 1
    elif i == 2:
        if pcs[i] > 2:
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:
            pcs[i] = pcs[i] + 2
    elif i == 3:
        if pcs[i] > 2:
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:
            pcs[i] = pcs[i] + 2
    elif i == 4:
        if pcs[i] > 2:
            pcs[i] = pcs[i] - 2
        elif pcs[i] < 2:
            pcs[i] = pcs[i] + 2
    elif i == 5:
        if pcs[i] > 8:
            pcs[i] = pcs[i] - 8
        elif pcs[i] < 8:
            pcs[i] = pcs[i] + 8

print(*pcs)
