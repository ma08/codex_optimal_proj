

N = int(input())

vaccinated = []
control = []

for i in range(N):
    participant = input()
    if participant[0] == "Y":
        vaccinated.append(participant[1:]) #slice the 'Y'
    else:
        control.append(participant[1:]) #slice the 'N'

def efficacy(infection_type):
    vaccinated_infection = sum(map(lambda x: int(x[infection_type]), vaccinated)) / len(vaccinated)
    control_infection = sum(map(lambda x: int(x[infection_type]), control)) / len(control)
    if vaccinated_infection < control_infection:
        return str((1 - vaccinated_infection/control_infection) * 100) + '%'
    return "Not Effective"

for i in range(3):
    print(efficacy(i))
