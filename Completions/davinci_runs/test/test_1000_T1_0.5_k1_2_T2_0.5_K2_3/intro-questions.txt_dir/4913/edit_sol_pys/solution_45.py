

n = int(input())

vaccinated = []
control = []

for i in range(n):
    line = input()
    if line[0] == 'Y':
        vaccinated.append(line)
    else:
        control.append(line)

strains = ['A', 'B', 'C']

for strain in strains:
    count = 0
    for person in vaccinated:
        if person[strains.index(strain) + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate1 = count / len(vaccinated)
    count = 0
    for person in control:
        if person[strains.index(strain) + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate2 = count / len(control)
    print(str(round(100 - rate1 / rate2 * 100, 2)) + "%")
