

import sys

# Read input
num_participants = int(sys.stdin.readline())
vaccinated = []
infected = []
for i in range(num_participants):
    participant = sys.stdin.readline()
    vaccinated.append(participant[0])
    infected.append(participant[1:])

# Calculate vaccine efficacy
# Count infected and not infected for each group
num_infected_vaccinated = 0
num_not_infected_vaccinated = 0
num_infected_control = 0
num_not_infected_control = 0
for j in range(num_participants):
    if infected[j] == 'Y':
        if vaccinated[j] == 'Y':
            num_infected_vaccinated += 1
        else:
            num_infected_control += 1
    else:
        if vaccinated[j] == 'Y':
            num_not_infected_vaccinated += 1
        else:
            num_not_infected_control += 1
# Calculate percentage infected for each group
percent_infected_vaccinated = num_infected_vaccinated / (num_infected_vaccinated + num_not_infected_vaccinated)
percent_infected_control = num_infected_control / (num_infected_control + num_not_infected_control)
# Calculate vaccine efficacy
if percent_infected_vaccinated < percent_infected_control:
    efficacy = 100 - percent_infected_vaccinated / percent_infected_control * 100
else:
    efficacy = "Not Effective"

# Print vaccine efficacy
print(efficacy)
