
N = int(input())

vaccinated = []
control = []

for i in range(N):
    participant = input().split(' ')
    if participant[0] == 'Y':
        vaccinated.append(list(map(int, participant[1:])))
    else:
        control.append(list(map(int, participant[1:])))

def efficacy(infection):
    vaccinated_infection = sum(map(lambda x: x[infection], vaccinated)) / len(vaccinated)
    control_infection = sum(map(lambda x: x[infection], control)) / len(control)
    if vaccinated_infection >= control_infection:
        return 'Not Effective'
    else:
        return str((1 - vaccinated_infection/control_infection) * 100)

for i in range(3):
    print(efficacy(i))
