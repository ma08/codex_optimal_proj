
N = int(input())

vaccinated = []
unvaccinated = []

for i in range(N):
    temp = input()
    if temp[0] == 'Y':
        vaccinated.append(temp)
    else:
        unvaccinated.append(temp)

strains = ['A', 'B', 'C']
for i in range(3):
    infected_v = 0
    infected_u = 0
    for j in range(len(vaccinated)):
        if vaccinated[j][i+1] == 'Y':
            infected_v += 1
    for j in range(len(unvaccinated)):
        if unvaccinated[j][i+1] == 'Y':
            infected_u += 1
    if infected_v == 0:
        print("Not effective")
    else:
        print(round(100 - (infected_v/len(vaccinated))/(infected_u/len(unvaccinated))*100, 2))
