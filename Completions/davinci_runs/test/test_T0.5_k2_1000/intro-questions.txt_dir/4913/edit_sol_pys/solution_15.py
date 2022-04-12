

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
    vaccinated_infection = sum(map(lambda x: x[infection], vaccinated)) / len(vaccinated) * 100
    control_infection = sum(map(lambda x: x[infection], control)) / len(control) * 100
    if vaccinated_infection >= control_infection:
        return 'Not effective'
    else:
        return str(1 - vaccinated_infection/control_infection)

for i in range(3):
    print(efficacy(i))
