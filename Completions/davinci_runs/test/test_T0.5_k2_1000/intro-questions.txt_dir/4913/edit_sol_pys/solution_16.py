

N = int(input())

vaccinated = []
control = []

for i in range(N):
    participant = input()
    if participant[0] == 'Y':
        vaccinated.append(participant[1:])
    else:
        control.append(participant[1:])

def efficacy(infection):
    vaccinated_infection = sum(map(lambda x: x[infection], vaccinated)) / len(vaccinated) * 100.0
    control_infection = sum(map(lambda x: x[infection], control)) / len(control) * 100.0
    if vaccinated_infection >= control_infection:
        return 'Not Effective'
    else:
        return str(round((1 - vaccinated_infection/control_infection) * 100, 2))

for i in range(3):
    print(efficacy(i))
