

pcs = [int(x) for x in input().split()]

for i in range(len(pcs)): #loop through the input
    if i == 0 and pcs[i] > 1:
        pcs[i] = pcs[i] - 1
    elif i == 0 and pcs[i] < 1:
        pcs[i] = pcs[i] + 1
    elif i == 1 and pcs[i] > 1:
        pcs[i] = pcs[i] - 1
    elif i == 1 and pcs[i] < 1:
        pcs[i] = pcs[i] + 1
    elif i == 2 and pcs[i] > 2:
        pcs[i] = pcs[i] - 2
    elif i == 2 and pcs[i] < 2:
        pcs[i] = pcs[i] + 2
    elif i == 3 and pcs[i] > 2:
        pcs[i] = pcs[i] - 2
    elif i == 3 and pcs[i] < 2:
        pcs[i] = pcs[i] + 2
    elif i == 4 and pcs[i] > 2:
        pcs[i] = pcs[i] - 2
    elif i == 4 and pcs[i] < 2:
        pcs[i] = pcs[i] + 2
    elif i == 5 and pcs[i] > 8:
        pcs[i] = pcs[i] - 8
    elif i == 5 and pcs[i] < 8:
        pcs[i] = pcs[i] + 8

print(*pcs)
