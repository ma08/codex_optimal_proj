
n = int(input())

vaccinated = []
control = []

for i in range(n):
    line = input()
    if line[0] == 'V':
        vaccinated.append(line)
    else:
        control.append(line)


for i in range(3):
    count = 0
    for person in vaccinated:
        if person[i + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate = count / len(vaccinated)
    count = 0
    for person in control:
        if person[i + 1] == 'Y':
            count += 1
    if count == 0:
        print("Not Effective")
        continue
    rate2 = count / len(control)
    print(100 - rate / rate2 * 100)
