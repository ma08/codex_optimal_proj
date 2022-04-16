

# Programmer:    Oliver Collins
# Date:          May 3rd, 2018
# Language:      Python

'''
----------------------
'''

# Snowy Winter
# Inputs number of years, and number of days between end of summer and first day of snow
# Outputs number of years that it had never snowed this early
def snowy_winter(n):
	count = 0
	for i in range(n):
		if int(input()) > d_m:
			count += 1
	return count

# Gets user input
n, d_m = input().split()

# Output, prints number of years it had never snowed this early
print("It hadn't snowed this early in", snowy_winter(int(n)), "years!")
