

N = int(input())

vaccinated = []
control = []

for i in range(N):
    participant = input()
    vaccinated.append(participant[1:])
    control.append(participant[1:])

def efficacy(infection):
    vaccinated_infection = sum(map(lambda x: int(x[infection]), vaccinated)) / len(vaccinated) * 100
    control_infection = sum(map(lambda x: int(x[infection]), control)) / len(control) * 100
    if vaccinated_infection >= control_infection:
        return 'Not Effective'
    else:
        return str((1 - vaccinated_infection/control_infection) * 100) + '%'

for i in range(3):
    print(efficacy(i))


