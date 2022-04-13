
import sys, math
 
# Read input
num_participants = int(sys.stdin.readline()) # Get the number of participants
vaccinated = [] # Create an empty list to store the vaccination status of each participant
infected = [] # Create an empty list to store the infection status of each participant
for i in range(num_participants): # For each participant
    participant = sys.stdin.readline() # Read the participant's data
    vaccinated.append(participant[0]) # Add the vaccination status to the list
    infected.append(participant[1:]) # Add the infection status to the list
 
# Calculate vaccine efficacies
efficacy = [] # Create an empty list to store the vaccine efficacy for each disease
for i in range(3): # For each disease
    # Count infected and not infected for each group (vaccinated and control)
    num_infected_vaccinated = 0 # The number of infected participants who were vaccinated
    num_not_infected_vaccinated = 0 # The number of not infected participants who were vaccinated
    num_infected_control = 0 # The number of infected participants who were not vaccinated
    num_not_infected_control = 0 # The number of not infected participants who were not vaccinated
    for j in range(num_participants): # For each participant
        if infected[j][i] == 'Y': # If the participant is infected
            if vaccinated[j] == 'Y': # If the participant was vaccinated
                num_infected_vaccinated += 1 # Increment the number of infected participants who were vaccinated
            else: # If the participant was not vaccinated
                num_infected_control += 1 # Increment the number of infected participants who were not vaccinated
        else: # If the participant is not infected
            if vaccinated[j] == 'Y': # If the participant was vaccinated
                num_not_infected_vaccinated += 1 # Increment the number of not infected participants who were vaccinated
            else: # If the participant was not vaccinated
                num_not_infected_control += 1 # Increment the number of not infected participants who were not vaccinated
    # Calculate percentage infected for each group (vaccinated and control)
    percent_infected_vaccinated = num_infected_vaccinated / (num_infected_vaccinated + num_not_infected_vaccinated) # The percentage of vaccinated participants who were infected
    percent_infected_control = num_infected_control / (num_infected_control + num_not_infected_control) # The percentage of not vaccinated participants who were infected
    # Calculate vaccine efficacy (the percentage of vaccinated participants who were not infected)
    if percent_infected_vaccinated < percent_infected_control: # If the percentage of vaccinated participants who were infected is less than the percentage of not vaccinated participants who were infected
        efficacy.append(100 - percent_infected_vaccinated / percent_infected_control * 100) # The vaccine is effective
    else: # If the percentage of vaccinated participants who were infected is greater than or equal to the percentage of not vaccinated participants who were infected
        efficacy.append("Not Effective") # The vaccine is not effective
 
# Print vaccine efficacies
print(efficacy[0]) # Print the vaccine efficacy for the first disease
print(efficacy[1]) # Print the vaccine efficacy for the second disease
print(efficacy[2]) # Print the vaccine efficacy for the third disease
