

n = int(input())

vaccinated = []
control = []

for i in range(n):
    line = input()
    if line[0] == 'V':
        vaccinated.append(line)
    else:
        control.append(line)

strains = ['A', 'B', 'C']

for strain in strains:
    count = 0
    for person in vaccinated:
        if person[strains.index(strain) + 1] == '1':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate = count / len(vaccinated)
    count = 0
    for person in control:
        if person[strains.index(strain) + 1] == '1':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate2 = count / len(control)
    print(100 - rate / rate2 * 100)
