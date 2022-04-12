

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
    if count == 0 or len(vaccinated) == 0:
        print("Not Effective")
        continue
    rate = count / len(vaccinated)
    count = 0
    for person in control:
        if person[strains.index(strain) + 1] == 'Y':
            count += 1
    if count == 0 or len(control) == 0:
        print("Not Effective")
        continue
    rate2 = count / len(control)
    print(100 - rate2 / rate * 100)
