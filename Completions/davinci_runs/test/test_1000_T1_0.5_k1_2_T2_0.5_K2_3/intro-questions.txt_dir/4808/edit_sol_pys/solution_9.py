

# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''

# Snowy Winter
# Inputs number of years and number of days between end of summer and first day of snow for this year
# Outputs number of years that it had never snowed this early for this year
def snowy_winter(n, d_m, d_m_less):
	count = 1
	for i in range(n-1): # Loops through all other years
		d_m_less = int(input()) # Gets number of days between end of summer and first day of snow for this year
		if d_m_less > d_m: # If this year had never snowed this early
			count += 1 # Add 1 to count
	return count # Return count

# Gets user input
n, d_m = map(int, input().split())

# Outputs number of years it had never snowed this early
print("It hadn't snowed this early in", snowy_winter(n, d_m), "years!")
