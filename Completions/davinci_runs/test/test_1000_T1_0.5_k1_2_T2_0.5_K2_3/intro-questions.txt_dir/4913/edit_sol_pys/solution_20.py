
N = int(input())
vaccinated = [input() for i in range(N)]
unvaccinated = [input() for i in range(N)]

strains = ['A', 'B', 'C']
for i in range(3):
    infected_v = sum(1 for j in vaccinated if j[i+1] == 'Y')
    infected_u = sum(1 for j in unvaccinated if j[i+1] == 'Y')
    if infected_v == 0: print("Not Effective")
    else: print(100 - (infected_v/len(vaccinated))/(infected_u/len(unvaccinated))*100, end=" ")
